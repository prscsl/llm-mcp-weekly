#!/usr/bin/env python3
"""
llm-mcp-weekly admin server.

로컬(127.0.0.1)에서만 실행되는 관리자 페이지.
launchd 시간 슬롯 관리, 수동 발행 트리거, 로그 보기 기능 제공.

실행:
    /Users/prscsl/.pyenv/versions/3.10.12/bin/python3 admin/server.py
    → http://127.0.0.1:7800
"""
from __future__ import annotations

import os
import plistlib
import re
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

from flask import Flask, abort, redirect, render_template, request, url_for

HOME = Path.home()
PROJECT_DIR = HOME / "llm-mcp-weekly"
PLIST_USER = HOME / "Library" / "LaunchAgents" / "com.prscsl.llm-mcp-weekly.daily.plist"
PLIST_REPO = PROJECT_DIR / "scripts" / "com.prscsl.llm-mcp-weekly.daily.plist"
LAUNCHD_LABEL = "com.prscsl.llm-mcp-weekly.daily"
RUN_DAILY = PROJECT_DIR / "scripts" / "run_daily.sh"
LOGS_DIR = PROJECT_DIR / "logs"
POSTS_DIR = PROJECT_DIR / "_posts"
MANUAL_LOG = Path("/tmp/llm-mcp-weekly.manual.log")
STDOUT_LOG = Path("/tmp/llm-mcp-weekly.stdout.log")

HOST = "127.0.0.1"
PORT = 7800

app = Flask(__name__)


def load_plist() -> dict:
    if not PLIST_USER.exists():
        abort(500, f"plist 없음: {PLIST_USER}")
    with PLIST_USER.open("rb") as f:
        return plistlib.load(f)


def save_plist(data: dict) -> None:
    """활성 사본 + 저장소 사본 양쪽 동기화."""
    payload = plistlib.dumps(data, sort_keys=False)
    PLIST_USER.write_bytes(payload)
    if PLIST_REPO.exists():
        # 저장소 사본의 주석(<!-- ... -->)은 plistlib이 보존하지 않으므로
        # 활성 사본만 진실 소스로 두고 저장소 사본은 동일 dump 결과로 덮어쓴다.
        PLIST_REPO.write_bytes(payload)


def get_schedule() -> list[dict]:
    """plist에서 시간 슬롯을 [{'hour': h, 'minute': m}] 리스트로 반환.
    단일 dict 또는 array 모두 처리."""
    data = load_plist()
    sci = data.get("StartCalendarInterval")
    if sci is None:
        return []
    if isinstance(sci, dict):
        return [{"hour": int(sci.get("Hour", 0)), "minute": int(sci.get("Minute", 0))}]
    out = []
    for d in sci:
        out.append({"hour": int(d.get("Hour", 0)), "minute": int(d.get("Minute", 0))})
    return out


def set_schedule(slots: list[dict]) -> None:
    if not slots:
        raise ValueError("시간 슬롯은 최소 1개 이상이어야 합니다.")
    # 시각 정렬 + 중복 제거
    uniq: dict[tuple[int, int], dict] = {}
    for s in slots:
        h = int(s["hour"]); m = int(s["minute"])
        if not (0 <= h <= 23) or not (0 <= m <= 59):
            raise ValueError(f"잘못된 시각: {h:02d}:{m:02d}")
        uniq[(h, m)] = {"Hour": h, "Minute": m}
    ordered = [uniq[k] for k in sorted(uniq.keys())]
    data = load_plist()
    if len(ordered) == 1:
        data["StartCalendarInterval"] = ordered[0]
    else:
        data["StartCalendarInterval"] = ordered
    save_plist(data)


def launchd_reload() -> tuple[bool, str]:
    """unload → load. (성공 여부, 합쳐진 출력)"""
    out_lines = []
    for action in ("unload", "load"):
        r = subprocess.run(
            ["launchctl", action, str(PLIST_USER)],
            capture_output=True, text=True
        )
        out_lines.append(f"launchctl {action}: rc={r.returncode}")
        if r.stdout: out_lines.append(r.stdout.strip())
        if r.stderr: out_lines.append(r.stderr.strip())
        if action == "load" and r.returncode != 0:
            return False, "\n".join(out_lines)
    return True, "\n".join(out_lines)


def launchd_loaded() -> bool:
    r = subprocess.run(["launchctl", "list"], capture_output=True, text=True)
    return any(LAUNCHD_LABEL in line for line in r.stdout.splitlines())


def running_pipeline_pids() -> list[tuple[int, str]]:
    """run_daily / collect / summarize / publish 중 실행 중인 PID·CMD."""
    r = subprocess.run(["ps", "-eo", "pid,command"], capture_output=True, text=True)
    out = []
    pat = re.compile(r"(run_daily\.sh|collect\.py|summarize\.py|publish\.py)")
    for line in r.stdout.splitlines()[1:]:
        line = line.strip()
        if not line or "grep" in line:
            continue
        if pat.search(line):
            try:
                pid_str, cmd = line.split(None, 1)
                out.append((int(pid_str), cmd))
            except ValueError:
                continue
    return out


def last_run_summary() -> dict:
    """logs/ 디렉토리에서 가장 최근 로그 파일과 마지막 줄."""
    if not LOGS_DIR.exists():
        return {"date": None, "last_line": None}
    logs = sorted(LOGS_DIR.glob("*.log"), reverse=True)
    if not logs:
        return {"date": None, "last_line": None}
    p = logs[0]
    try:
        last_line = p.read_text(encoding="utf-8").rstrip().splitlines()[-1]
    except (OSError, IndexError):
        last_line = None
    return {"date": p.stem, "last_line": last_line, "path": str(p)}


def recent_posts(n: int = 5) -> list[str]:
    if not POSTS_DIR.exists():
        return []
    files = sorted(POSTS_DIR.glob("*-llm-mcp-daily.md"), reverse=True)
    return [f.name for f in files[:n]]


def read_log(date: str | None) -> tuple[str | None, str]:
    """date(YYYY-MM-DD)에 해당하는 로그 본문. date=None이면 가장 최근."""
    if not LOGS_DIR.exists():
        return None, ""
    if date is None:
        logs = sorted(LOGS_DIR.glob("*.log"), reverse=True)
        if not logs:
            return None, ""
        target = logs[0]
    else:
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
            abort(400, "잘못된 날짜 형식")
        target = LOGS_DIR / f"{date}.log"
        if not target.exists():
            return target.stem, ""
    return target.stem, target.read_text(encoding="utf-8", errors="replace")


def available_log_dates() -> list[str]:
    if not LOGS_DIR.exists():
        return []
    return sorted([p.stem for p in LOGS_DIR.glob("*.log")], reverse=True)


def trigger_manual_run() -> tuple[bool, str]:
    """nohup으로 run_daily.sh background 실행."""
    if running_pipeline_pids():
        return False, "이미 실행 중인 파이프라인이 있습니다. 먼저 정리하세요."
    if not RUN_DAILY.exists():
        return False, f"실행 스크립트 없음: {RUN_DAILY}"
    log_target = MANUAL_LOG.open("ab")
    try:
        subprocess.Popen(
            ["/bin/zsh", str(RUN_DAILY)],
            cwd=str(PROJECT_DIR),
            stdout=log_target, stderr=subprocess.STDOUT,
            start_new_session=True,
        )
    finally:
        log_target.close()
    return True, f"백그라운드 실행 시작 — 로그: {MANUAL_LOG}"


def kill_pipeline(pids: list[int]) -> tuple[int, list[str]]:
    """주어진 PID들에 SIGTERM."""
    msgs = []
    killed = 0
    for pid in pids:
        try:
            os.kill(pid, 15)  # SIGTERM
            killed += 1
            msgs.append(f"kill -TERM {pid}: ok")
        except ProcessLookupError:
            msgs.append(f"kill -TERM {pid}: 이미 종료됨")
        except PermissionError:
            msgs.append(f"kill -TERM {pid}: 권한 없음")
    return killed, msgs


# ----- routes -----

@app.before_request
def restrict_to_localhost():
    """외부 IP 접근 차단 (혹시 모를 노출 대비)."""
    if request.remote_addr not in ("127.0.0.1", "::1"):
        abort(403, "localhost only")


@app.route("/")
def index():
    flash = request.args.get("flash") or ""
    flash_kind = request.args.get("kind") or "info"
    log_date = request.args.get("log_date")
    selected_log_date, log_body = read_log(log_date)
    return render_template(
        "index.html",
        schedule=get_schedule(),
        launchd_loaded=launchd_loaded(),
        last_run=last_run_summary(),
        recent=recent_posts(5),
        running=running_pipeline_pids(),
        log_dates=available_log_dates(),
        selected_log_date=selected_log_date,
        log_body=log_body,
        manual_log_exists=MANUAL_LOG.exists(),
        flash=flash,
        flash_kind=flash_kind,
        plist_user=str(PLIST_USER),
        now=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )


@app.route("/schedule/add", methods=["POST"])
def schedule_add():
    raw = request.form.get("time", "").strip()
    m = re.fullmatch(r"(\d{1,2}):(\d{2})", raw)
    if not m:
        return redirect(url_for("index", flash=f"시각 형식 오류: '{raw}' (HH:MM)", kind="error"))
    hour, minute = int(m.group(1)), int(m.group(2))
    try:
        current = get_schedule()
        current.append({"hour": hour, "minute": minute})
        set_schedule(current)
        ok, log = launchd_reload()
        msg = f"{hour:02d}:{minute:02d} 추가됨. " + ("재로드 OK." if ok else f"재로드 실패: {log}")
        return redirect(url_for("index", flash=msg, kind="ok" if ok else "error"))
    except ValueError as e:
        return redirect(url_for("index", flash=str(e), kind="error"))


@app.route("/schedule/delete", methods=["POST"])
def schedule_delete():
    try:
        idx = int(request.form.get("index", "-1"))
        current = get_schedule()
        if not (0 <= idx < len(current)):
            return redirect(url_for("index", flash="잘못된 인덱스", kind="error"))
        if len(current) <= 1:
            return redirect(url_for("index", flash="최소 1개 슬롯은 유지해야 합니다", kind="error"))
        removed = current.pop(idx)
        set_schedule(current)
        ok, log = launchd_reload()
        msg = f"{removed['hour']:02d}:{removed['minute']:02d} 삭제됨. " + ("재로드 OK." if ok else f"재로드 실패: {log}")
        return redirect(url_for("index", flash=msg, kind="ok" if ok else "error"))
    except (ValueError, TypeError):
        return redirect(url_for("index", flash="잘못된 요청", kind="error"))


@app.route("/run-now", methods=["POST"])
def run_now():
    ok, msg = trigger_manual_run()
    return redirect(url_for("index", flash=msg, kind="ok" if ok else "error"))


@app.route("/kill", methods=["POST"])
def kill_now():
    pids = [pid for pid, _ in running_pipeline_pids()]
    if not pids:
        return redirect(url_for("index", flash="실행 중인 파이프라인 없음", kind="info"))
    killed, msgs = kill_pipeline(pids)
    return redirect(url_for("index", flash=f"{killed}개 종료 — " + "; ".join(msgs), kind="ok"))


@app.route("/reload", methods=["POST"])
def reload_launchd():
    ok, log = launchd_reload()
    return redirect(url_for("index", flash="재로드: " + ("OK" if ok else log), kind="ok" if ok else "error"))


@app.route("/manual-log")
def manual_log_view():
    if not MANUAL_LOG.exists():
        body = "(아직 수동 실행 로그가 없습니다.)"
    else:
        try:
            body = MANUAL_LOG.read_text(encoding="utf-8", errors="replace")[-20000:]
        except OSError as e:
            body = f"(로그 읽기 실패: {e})"
    return render_template("manual_log.html", body=body, path=str(MANUAL_LOG))


if __name__ == "__main__":
    print(f"[admin] http://{HOST}:{PORT}  (localhost only)")
    app.run(host=HOST, port=PORT, debug=False)

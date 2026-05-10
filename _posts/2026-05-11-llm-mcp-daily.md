---
layout: post
title: "2026-05-11 LLM·MCP 위클리"
date: 2026-05-11 09:00:00 +0900
categories: [weekly]
tags: [ai 논문작성, ai 코딩, ai-alignment, ai-에이전트, ai업계동향, ai인프라, ai코딩도구, alphaevolve, anthropic, claude, claude code, claude-code, claude-mythos, cli, coding-agent, firefox, fst, gemini 3.1 flash-lite, github, google ai, google deepmind, gpt-5, html, httpx, ide-extension, interpretability, llm-gemini, llm-보안, llm-연구, llm-훈련, llm시장, llm활용, mcp, openai, pydantic, python-sdk, sqlite, vibe-coding, vscode, webrtc, whisper, worktree, xai, 개발도구, 개발자도구, 개발자성장, 데이터센터, 바퀴재발명, 버전관리, 보안강화, 보안취약점, 샌드박스, 실시간음성api, 실시간통신, 오픈소스, 음성ai, 자동화-취약점-분석, 프레젠테이션, 프롬프트 엔지니어링, 학술연구]
---

## 2026-05-11 한국어 LLM·MCP 큐레이션

오늘 큐레이션된 항목: 총 **29건**. 
Anthropic, MCP 생태계, HuggingFace, HackerNews 등에서 자동 수집·요약했습니다.

### 릴리스 소식 (7)
{: .cat-section .cat-release}

#### Claude Code v2.1.138 마이너 패치 릴리스

Anthropic의 AI 코딩 도구 Claude Code가 v2.1.138로 업데이트되었습니다. 이번 릴리스는 내부 버그 수정 위주의 소규모 패치로, 사용자 대상 새 기능이나 주요 변경 사항은 포함되지 않았습니다. 활발한 릴리스 주기가 유지되고 있어, Claude Code를 CI/CD나 개발 워크플로에 통합 중인 팀이라면 안정성 개선 차원에서 업데이트를 권장합니다.

[원문 보기 →](https://github.com/anthropics/claude-code/releases/tag/v2.1.138) (GitHub: anthropics/claude-code)

#### Claude Code v2.1.137: Windows VSCode 확장 활성화 버그 수정

Anthropic의 AI 코딩 도구 Claude Code가 v2.1.137을 릴리스했다. 이번 업데이트는 Windows 환경에서 VSCode 확장이 정상적으로 활성화되지 않던 문제를 수정한 패치 릴리스다. 규모는 작지만, Windows에서 Claude Code VSCode 확장을 사용하던 개발자라면 즉시 업데이트할 필요가 있다. Claude Code를 주력 코딩 보조 도구로 채택한 팀이라면 안정성 확보 차원에서 버전 관리에 신경 쓸 시점이다.

[원문 보기 →](https://github.com/anthropics/claude-code/releases/tag/v2.1.137) (GitHub: anthropics/claude-code)

#### Claude Code v2.1.136: MCP 서버 인증·세션 안정성 대폭 개선

Claude Code 2.1.136은 MCP OAuth 토큰 동시 갱신 시 유실되던 문제를 수정해, 여러 원격 MCP 서버를 사용하는 환경에서 매일 재인증할 필요가 없어졌다. VS Code·JetBrains 확장에서 /clear 후 MCP 서버가 사라지는 버그와, 경로에 언더스코어가 포함된 프로젝트에서 세션 복원이 실패하는 문제도 해결됐다. 엔터프라이즈용 OTEL 피드백 설정과 auto mode 강제 차단 규칙(hard_deny)이 추가되어, 사내 MCP 기반 에이전트 운영 시 정책 제어가 한층 세밀해졌다.

[원문 보기 →](https://github.com/anthropics/claude-code/releases/tag/v2.1.136) (GitHub: anthropics/claude-code)

#### Claude Code v2.1.133: worktree 분기 설정과 안정성 개선

Claude Code v2.1.133에서 worktree 생성 시 분기 기준을 origin/default 또는 로컬 HEAD 중 선택할 수 있는 worktree.baseRef 설정이 추가되었다. 훅에서 현재 effort 레벨을 환경변수로 참조할 수 있게 되었고, 메모리 압박 시 백그라운드 워커를 해제하는 최적화도 포함되었다. 병렬 세션에서 토큰 갱신 경합으로 전체 세션이 401 오류에 빠지는 버그 등 여러 안정성 문제가 수정되어, 팀 단위로 Claude Code를 활용하는 개발 환경에서 체감 안정성이 높아질 것으로 보인다.

[원문 보기 →](https://github.com/anthropics/claude-code/releases/tag/v2.1.133) (GitHub: anthropics/claude-code)

#### MCP Python SDK v1.27.1: Pydantic 2.13 호환성 및 httpx 버전 제한

MCP Python SDK v1.27.1이 출시되어 Pydantic 2.13에서 출력 스키마 생성 시 발생하던 오류를 수정하고, OAuth 메타데이터의 빈 문자열 처리 문제를 해결했다. 또한 httpx 1.0.0 미만으로 의존성을 제한하여 호환성 문제를 사전에 방지한다. Pydantic이나 httpx를 최신 버전으로 업그레이드한 환경에서 MCP 서버를 운영 중이라면 즉시 업데이트를 권장한다.

[원문 보기 →](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v1.27.1) (GitHub: modelcontextprotocol/python-sdk)

#### llm-gemini 0.31 출시 — Gemini 3.1 Flash-Lite GA 지원

Simon Willison의 LLM CLI 플러그인 llm-gemini가 0.31로 업데이트되며 Gemini 3.1 Flash-Lite 모델의 정식(GA) 전환을 반영했다. 해당 모델은 3월 프리뷰 이후 사양 변경 없이 GA로 승격된 것으로, 경량 추론이 필요한 프로덕션 환경에서 안정적으로 사용할 수 있게 되었다. 터미널에서 다양한 LLM을 통합 호출하는 워크플로를 구축 중인 개발자라면 llm-gemini 플러그인을 통해 Gemini 모델군을 간편하게 활용할 수 있다.

[원문 보기 →](https://simonwillison.net/2026/May/7/llm-gemini/#atom-everything) (Simon Willison)

#### OpenAI 실시간 음성 API 대폭 강화: Realtime-2, Translate, Whisper 출시

OpenAI가 GPT-5 기반 실시간 음성 처리 API 라인업을 확장했다. Realtime-2는 기존 대비 향상된 음성 대화 품질을 제공하며, Translate API는 실시간 통역, Whisper는 음성 인식 분야에서 새로운 성능 기준을 세웠다. 한국 개발자에게는 다국어 음성 서비스 구축 시 자체 파이프라인 대신 단일 API로 처리할 수 있는 선택지가 늘어난 점이 실질적으로 의미 있다.

[원문 보기 →](https://www.latent.space/p/ainews-gpt-realtime-2-translate-and) (Latent Space)

### 도구 / 라이브러리 (5)
{: .cat-section .cat-tool}

#### re_gent: AI 코딩 에이전트 활동을 추적하는 버전 관리 도구

AI 코딩 에이전트(Claude Code 등)가 코드베이스에서 수행한 모든 도구 호출을 자동으로 기록하고, 어떤 프롬프트가 어떤 코드를 작성했는지 blame 추적할 수 있는 Go 기반 CLI 도구다. .regent/ 디렉토리에 BLAKE3 해시 기반 DAG 구조로 변경 이력을 저장하며, 세션별 로그 조회와 특정 시점으로의 되감기를 지원한다. AI 에이전트에게 코드 수정 권한을 주면서도 변경 추적이 불가능했던 문제를 해결하므로, 에이전트 기반 개발 워크플로를 도입한 팀에서 디버깅과 감사 용도로 활용할 수 있다.

> HN 118점 · [토론 보기](https://news.ycombinator.com/item?id=48063548)

[원문 보기 →](https://github.com/regent-vcs/re_gent) (HN (claude))

#### Claude Code용 학술 연구 스킬 모음 — 논문 작성 파이프라인 자동화

Claude Code에서 학술 논문의 문헌조사, 집필, 피어리뷰, 인용 검증까지 전 과정을 지원하는 오픈소스 스킬 패키지다. 13개 에이전트 기반 심층 리서치, 12개 에이전트 논문 작성, 7개 에이전트 리뷰 등 10단계 파이프라인을 제공하며, Semantic Scholar API 검증과 허위 인용 탐지 등 무결성 게이트를 내장했다. AI가 대신 쓰는 것이 아닌 human-in-the-loop 원칙을 강조하는 점이 특징으로, LLM 기반 코딩 도구를 연구 워크플로에 접목하려는 개발자·연구자에게 참고할 만한 설계 패턴을 보여준다.

> HN 72점 · [토론 보기](https://news.ycombinator.com/item?id=48083919)

[원문 보기 →](https://github.com/Imbad0202/academic-research-skills) (HN (claude))

#### re_gent: AI 코딩 에이전트 활동을 추적하는 버전 관리 도구

AI 코딩 에이전트(Claude Code 등)가 코드베이스에서 수행한 모든 도구 호출을 자동으로 기록하고, 어떤 프롬프트가 어떤 코드를 작성했는지 blame 추적할 수 있는 Go 기반 CLI 도구다. .regent/ 디렉토리에 BLAKE3 해시 기반 DAG 구조로 변경 이력을 저장하며, 세션별 로그 조회와 특정 시점으로의 되감기를 지원한다. AI 에이전트에게 코드 수정 권한을 주면서도 변경 추적이 불가능했던 문제를 해결하므로, 에이전트 기반 개발 워크플로를 도입한 팀에서 디버깅과 감사 용도로 활용할 수 있다.

> HN 118점 · [토론 보기](https://news.ycombinator.com/item?id=48063548)

[원문 보기 →](https://github.com/regent-vcs/re_gent) (HN (agentic))

#### Simon Willison의 Big Words — URL 기반 텍스트 슬라이드 생성 도구

Simon Willison이 자신의 macOS 프레젠테이션 도구에서 텍스트 슬라이드를 표시하기 위해 쿼리스트링으로 텍스트·색상·그라디언트·폰트를 제어할 수 있는 단일 페이지 도구를 만들었다. 더블클릭으로 설정 패널을 열어 실시간 편집이 가능하며, URL 자체가 슬라이드 상태를 담고 있어 별도 저장 없이 공유할 수 있다. URL-as-config 패턴은 간단한 내부 도구를 빠르게 만들 때 참고할 만한 접근법이다.

[원문 보기 →](https://simonwillison.net/2026/May/7/big-words/#atom-everything) (Simon Willison)

#### GitHub 저장소 통계를 한눈에 확인하는 웹 도구

GitHub 모바일 화면에서는 커밋 수 등 핵심 통계가 보이지 않는 불편함이 있다. Simon Willison이 GitHub REST/GraphQL API를 CORS fetch로 호출해 저장소의 커밋 수와 주요 지표를 바로 확인할 수 있는 간단한 웹 도구를 만들었다. 오픈소스 라이브러리나 도구를 평가할 때 빠르게 활성도를 판단하는 용도로 유용하다.

[원문 보기 →](https://simonwillison.net/2026/May/7/github-repo-stats/#atom-everything) (Simon Willison)

### 업계 뉴스 (5)
{: .cat-section .cat-news}

#### Mozilla, Claude Mythos Preview 활용해 Firefox 보안 강화 사례 공개

Mozilla가 Anthropic의 Claude Mythos Preview 모델을 활용하여 Firefox 브라우저의 보안 취약점을 탐지하고 코드를 강화한 과정을 공개했다. LLM을 정적 분석 보조 도구로 사용해 메모리 안전성 문제와 잠재적 공격 표면을 식별하는 워크플로를 구축한 것이 핵심이다. 대규모 C++ 코드베이스를 다루는 국내 시스템 엔지니어에게 LLM 기반 보안 감사 자동화의 실전 참고 사례가 될 수 있다.

> HN 378점 · [토론 보기](https://news.ycombinator.com/item?id=48051079)

[원문 보기 →](https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/) (HN (claude))

#### Claude Code 심링크 샌드박스 탈출 취약점(CVE-2026-39861) 공개

Claude Code에서 심볼릭 링크를 이용해 샌드박스를 우회할 수 있는 보안 취약점이 발견되어 CVE-2026-39861로 등록됐다. 공격자가 악의적 심링크를 프로젝트 디렉토리에 배치하면 Claude Code의 파일 시스템 격리를 벗어나 임의 경로에 접근할 수 있는 문제다. AI 코딩 에이전트를 실무에 도입한 팀이라면 즉시 패치 적용 여부를 확인하고, 에이전트가 작업하는 디렉토리의 심링크 존재 여부를 점검할 필요가 있다.

> HN 51점 · [토론 보기](https://news.ycombinator.com/item?id=48057842)

[원문 보기 →](https://github.com/advisories/GHSA-vp62-r36r-9xqp) (HN (claude))

#### Mozilla, Claude Mythos 활용해 Firefox 보안 취약점 수백 건 발견·수정

Mozilla가 Anthropic의 Claude Mythos 프리뷰를 활용해 Firefox에서 수백 건의 보안 취약점을 찾아 수정한 과정을 공개했다. 20년 된 XSLT 버그, 15년 된 legend 요소 버그 등 오래된 결함도 포함되며, 모델 성능 향상과 하네스 기법(모델 조합·스케일링·노이즈 필터링) 개선이 핵심이었다고 밝혔다. 불과 몇 달 전까지 LLM 보안 리포트는 슬롭 취급을 받았으나 이제 실제 프로덕션 코드베이스에서 유의미한 결과를 내는 단계에 진입했다는 점에서, 국내 대규모 C/C++ 프로젝트에도 유사한 자동화 보안 감사 도입을 검토할 시점이다.

[원문 보기 →](https://simonwillison.net/2026/May/7/firefox-claude-mythos/#atom-everything) (Simon Willison)

#### Anthropic 연 10배 성장, AI 업계 양극화 심화

Anthropic이 연간 10배 규모로 급성장하는 동안, 다수의 AI 기업들은 10% 이상 인력을 감축하고 있어 업계 내 양극화가 뚜렷해지고 있다. 기반 모델을 직접 개발하는 소수 기업에 인재와 자본이 집중되는 반면, 래퍼(wrapper) 서비스나 차별화가 부족한 스타트업은 구조조정 압박을 받는 구도다. 한국 개발자 입장에서는 Claude 생태계(MCP, API)처럼 플랫폼 지위를 가진 도구에 역량을 집중하는 것이 리스크 관리에 유리할 수 있다.

[원문 보기 →](https://www.latent.space/p/ainews-anthropic-growing-10xyear) (Latent Space)

#### Anthropic, xAI 콜로서스 데이터센터에 300MW 규모 계약 체결

Anthropic이 xAI(구 SpaceX AI)의 콜로서스 I 데이터센터와 연간 50억 달러 규모, 300MW 전력 사용 계약을 맺은 것으로 알려졌다. Anthropic의 연간 반복 매출(ARR) 성장률은 연환산 기준 8000%에 달하며, 대규모 컴퓨팅 인프라 확보 경쟁이 본격화되고 있다. 한국 AI 인프라 기업과 클라우드 엔지니어 입장에서 GPU 클러스터 임대·전력 계약 모델의 산업 표준이 어떻게 형성되는지 주목할 필요가 있다.

[원문 보기 →](https://www.latent.space/p/ainews-anthropic-spacexais-300mw5byr) (Latent Space)

### 연구 / 논문 (6)
{: .cat-section .cat-research}

#### Anthropic, Claude 내부 사고를 자연어로 변환하는 오토인코더 연구 공개

Anthropic이 LLM 내부 표현(representation)을 사람이 읽을 수 있는 자연어로 인코딩하고 다시 복원하는 '자연어 오토인코더' 기법을 발표했다. 기존 해석가능성(interpretability) 연구가 뉴런 단위 분석에 집중했다면, 이 접근은 모델의 사고 과정 자체를 텍스트로 추출해 검증할 수 있는 경로를 제시한다. AI 안전성과 디버깅에 관심 있는 한국 개발자라면, LLM의 블랙박스 문제를 해소하는 새로운 방법론으로 주목할 만하다.

> HN 367점 · [토론 보기](https://news.ycombinator.com/item?id=48052537)

[원문 보기 →](https://www.anthropic.com/research/natural-language-autoencoders) (HN (claude))

#### Anthropic의 Claude 훈련 방법론: 왜(Why)를 가르치는 접근법

Anthropic이 Claude 모델에 단순 규칙 준수가 아닌 '왜 그렇게 행동해야 하는지' 이유를 학습시키는 연구를 공개했다. 규칙 기반 정렬 대신 원리와 맥락을 이해시켜 새로운 상황에서도 적절한 판단을 내릴 수 있도록 하는 것이 핵심이다. 프롬프트 엔지니어링이나 시스템 프롬프트 설계 시 '왜'를 명시하는 것이 모델 성능에 직접 영향을 줄 수 있음을 시사하므로, LLM 기반 서비스를 구축하는 개발자라면 참고할 만한 연구다.

> HN 258점 · [토론 보기](https://news.ycombinator.com/item?id=48066592)

[원문 보기 →](https://www.anthropic.com/research/teaching-claude-why) (HN (claude))

#### 구글 딥마인드 AlphaEvolve: Gemini 기반 코딩 에이전트로 다양한 분야 문제 해결

구글 딥마인드가 Gemini 모델을 활용한 코딩 에이전트 AlphaEvolve를 공개했다. 이 에이전트는 진화적 알고리즘과 LLM을 결합해 수학, 과학, 컴퓨팅 등 여러 분야에서 기존 알고리즘을 자동으로 개선하거나 새로운 해법을 탐색한다. HN에서 326포인트·148개 댓글을 기록하며 높은 관심을 받았으며, 코딩 에이전트가 단순 코드 생성을 넘어 알고리즘 최적화·탐색 도구로 확장되고 있다는 점에서 한국 엔지니어들도 주목할 만하다.

> HN 326점 · [토론 보기](https://news.ycombinator.com/item?id=48050278)

[원문 보기 →](https://deepmind.google/blog/alphaevolve-impact/) (HN (coding agent))

#### Anthropic, Claude 내부 사고를 자연어로 변환하는 오토인코더 연구 공개

Anthropic이 LLM 내부 표현(representation)을 사람이 읽을 수 있는 자연어로 인코딩하고 다시 복원하는 '자연어 오토인코더' 기법을 발표했다. 기존 해석가능성(interpretability) 연구가 뉴런 단위 분석에 집중했다면, 이 접근은 모델의 사고 과정 자체를 텍스트로 추출해 검증할 수 있는 경로를 제시한다. AI 안전성과 디버깅에 관심 있는 한국 개발자라면, LLM의 블랙박스 문제를 해소하는 새로운 방법론으로 주목할 만하다.

> HN 367점 · [토론 보기](https://news.ycombinator.com/item?id=48052537)

[원문 보기 →](https://www.anthropic.com/research/natural-language-autoencoders) (HN (anthropic))

#### Anthropic의 Claude 훈련 방법론: 왜(Why)를 가르치는 접근법

Anthropic이 Claude 모델에 단순 규칙 준수가 아닌 '왜 그렇게 행동해야 하는지' 이유를 학습시키는 연구를 공개했다. 규칙 기반 정렬 대신 원리와 맥락을 이해시켜 새로운 상황에서도 적절한 판단을 내릴 수 있도록 하는 것이 핵심이다. 프롬프트 엔지니어링이나 시스템 프롬프트 설계 시 '왜'를 명시하는 것이 모델 성능에 직접 영향을 줄 수 있음을 시사하므로, LLM 기반 서비스를 구축하는 개발자라면 참고할 만한 연구다.

> HN 258점 · [토론 보기](https://news.ycombinator.com/item?id=48066592)

[원문 보기 →](https://www.anthropic.com/research/teaching-claude-why) (HN (anthropic))

#### 구글 딥마인드 AlphaEvolve: Gemini 기반 코딩 에이전트로 다양한 분야 문제 해결

구글 딥마인드가 Gemini 모델을 활용한 코딩 에이전트 AlphaEvolve를 공개했다. 이 에이전트는 진화적 알고리즘과 LLM을 결합해 수학, 과학, 컴퓨팅 등 여러 분야에서 기존 알고리즘을 자동으로 개선하거나 새로운 해법을 탐색한다. HN에서 326포인트·148개 댓글을 기록하며 높은 관심을 받았으며, 코딩 에이전트가 단순 코드 생성을 넘어 알고리즘 최적화·탐색 도구로 확장되고 있다는 점에서 한국 엔지니어들도 주목할 만하다.

> HN 326점 · [토론 보기](https://news.ycombinator.com/item?id=48050278)

[원문 보기 →](https://deepmind.google/blog/alphaevolve-impact/) (HN (agentic))

### 의견 / 분석 (6)
{: .cat-section .cat-opinion}

#### Claude Code에서 HTML이 비합리적으로 효과적인 이유

Claude Code로 작업할 때 React나 복잡한 프레임워크 대신 순수 HTML을 활용하면 놀라울 정도로 높은 품질의 결과물을 얻을 수 있다는 경험이 HN에서 큰 반향을 일으켰다(503포인트, 270댓글). AI 코딩 에이전트가 단순한 마크업 구조를 더 정확하게 생성·수정할 수 있어, 프로토타이핑 속도와 정확도가 크게 향상된다는 내용이다. 한국 개발자들도 AI 코딩 도구 활용 시 기술 스택 선택이 결과 품질에 직접 영향을 준다는 점을 고려할 필요가 있다.

> HN 503점 · [토론 보기](https://news.ycombinator.com/item?id=48071940)

[원문 보기 →](https://twitter.com/trq212/status/2052809885763747935) (HN (claude))

#### AI 에이전트 친화적 CLI 설계 원칙

AI 에이전트가 기존 CLI 도구를 효과적으로 활용하려면 구조화된 출력, 명확한 에러 메시지, 비대화형 모드 등 에이전트 친화적 설계가 필요하다는 원칙을 제시한다. MCP 같은 도구 호출 프로토콜이 확산되는 시점에서, CLI 도구 개발자라면 에이전트가 파싱하기 쉬운 인터페이스 설계를 고려할 필요가 있다. HN에서 110포인트·50개 댓글로 활발한 논의가 이루어졌으며, 한국 백엔드 엔지니어에게는 기존 내부 CLI 도구를 에이전트 워크플로에 통합할 때 실질적인 가이드라인이 될 수 있다.

> HN 110점 · [토론 보기](https://news.ycombinator.com/item?id=48052333)

[원문 보기 →](https://twitter.com/trevin/status/2051316002730991795) (HN (agentic))

#### 바퀴를 재발명하는 것이 실력 향상의 지름길인 이유

Andrew Quinn은 3GB SQLite 데이터베이스를 7MB FST(유한 상태 변환기) 바이너리로 대체한 글의 각주에서, 이미 존재하는 도구를 다시 만드는 '바퀴의 재발명'이 오히려 해당 분야의 최전선에 도달하는 가장 빠른 방법이라고 주장한다. 천 개도, 영 개도 아닌 네다섯 개 정도의 바퀴를 직접 만들어보고, 그 과정에서 던지는 질문들이 같은 시간의 수동적 학습보다 훨씬 효과적이라는 것이다. 기존 라이브러리에 의존하기 쉬운 한국 개발 환경에서, 핵심 자료구조나 알고리즘을 직접 구현해보는 경험의 가치를 다시 생각하게 하는 관점이다.

[원문 보기 →](https://simonwillison.net/2026/May/10/andrew-quinn/#atom-everything) (Simon Willison)

#### WebRTC가 LLM 음성 API에 부적합한 이유

Discord 출신 개발자 Luke Curley가 OpenAI의 음성 AI 인프라에 WebRTC를 사용하는 방식의 근본적 한계를 지적했다. WebRTC는 화상회의용으로 설계되어 네트워크 불안정 시 오디오 패킷을 공격적으로 드롭하는데, LLM 프롬프트 전송에서는 200ms를 더 기다리더라도 정확한 입력이 전달되는 것이 훨씬 중요하다. 브라우저 내에서 WebRTC 오디오 패킷 재전송 자체가 불가능하게 하드코딩되어 있어 근본적 해결이 어렵다는 점도 강조했다. 음성 기반 AI 서비스를 설계하는 한국 개발자라면 WebRTC의 실시간 최적화가 LLM 유스케이스와 상충할 수 있음을 인지하고, 대안 프로토콜 검토가 필요하다.

[원문 보기 →](https://simonwillison.net/2026/May/9/luke-curley/#atom-everything) (Simon Willison)

#### Claude Code에서 Markdown 대신 HTML 출력을 요청하면 생기는 일

Anthropic Claude Code 팀의 Thariq Shihipar가 LLM 출력 포맷으로 Markdown 대신 HTML을 요청할 때의 이점을 정리했다. HTML로 출력하면 SVG 다이어그램, 인터랙티브 위젯, 페이지 내 네비게이션 등 훨씬 풍부한 시각적 표현이 가능해 PR 리뷰나 개념 설명 같은 작업에서 정보 전달력이 크게 높아진다. GPT-4 시절 토큰 제한 때문에 Markdown이 효율적이었지만, 컨텍스트 윈도우가 커진 지금은 출력 포맷을 재고할 시점이다. 프롬프트 엔지니어링에서 출력 형식 지정이 결과 품질에 미치는 영향을 보여주는 실용적 사례로, Claude Code 활용도를 높이려는 개발자라면 참고할 만하다.

[원문 보기 →](https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/#atom-everything) (Simon Willison)

#### Anthropic, xAI 콜로서스 데이터센터 임대 계약의 의미와 논란

Anthropic이 Code w/ Claude 행사에서 xAI의 콜로서스 데이터센터 전체 용량을 임대하는 계약을 발표했다. 해당 시설은 대기오염 허가 없이 가스터빈을 가동해 환경 문제를 일으킨 전력이 있어 논란이 되고 있다. AI 데이터센터의 환경 영향이 정치적 이슈로 부상한 상황에서 컴퓨팅 자원 확보를 위한 현실적 선택이 브랜드 리스크로 이어질 수 있다는 점은 인프라 전략을 고민하는 엔지니어에게도 시사점을 준다.

[원문 보기 →](https://simonwillison.net/2026/May/7/xai-anthropic/#atom-everything) (Simon Willison)

---
layout: page
title: 이 사이트에 대해
permalink: /about/
---

## LLM·MCP 위클리란

**LLM·MCP 위클리**는 Claude·MCP(Model Context Protocol)·LLM 생태계의 영문 소식을 매일 자동 수집하고, Claude로 한국어 요약·큐레이션하여 발행하는 기술 뉴스 블로그입니다.

타겟 독자는 한국의 백엔드/데이터 엔지니어 중 AI 도구를 실무에 통합하려는 분들입니다. 단순 번역이 아니라, **"현업 엔지니어 관점에서 이게 왜 중요한가"** 를 기준으로 내용을 선별합니다.

---

## 운영자

**박성수 (prscsl)**

- 데이터 파이프라인 및 자동화 엔지니어
- Claude Code 일상 사용자 (데이터 전송 자동화, 오픈소스 배포 자동화, MCP 서버 개발 등에 실무 활용 중)
- Apache SeaTunnel 기반 자동 배포·모니터링 플랫폼 개발, Airflow DAG 템플릿 시스템, CloudBeaver 포크 개발
- GitHub: [github.com/prscsl](https://github.com/prscsl)

이 블로그는 개인 학습 및 커뮤니티 기여 목적으로 운영됩니다.

---

## 콘텐츠 수집 및 발행 방식

### 자동화 파이프라인

매일 아침 6시(KST) 자동 실행되며 다음 순서로 콘텐츠가 생성됩니다:

1. **수집** — 주요 영문 기술 뉴스 소스(Hacker News, GitHub Releases, 공식 블로그 RSS)에서 LLM·MCP·Claude 관련 항목 필터링
2. **요약** — 수집된 원문을 Claude API로 전달하여 한국어 요약 생성
3. **발행** — Jekyll 포스트로 자동 빌드 후 GitHub Pages에 배포

### AI 사용 고지

이 사이트의 요약 콘텐츠는 **Anthropic의 Claude가 생성**합니다. 원문 출처는 각 포스트에 명시됩니다. 운영자가 파이프라인 코드와 프롬프트를 직접 관리하며, 발행 전 품질 점검을 수행합니다.

---

## 콘텐츠 정책

- **출처 명시** — 모든 포스트에 원문 URL과 출처를 표기합니다.
- **저작권 준수** — 원문 전문을 복제하지 않으며, 요약 및 코멘트 형식으로 제공합니다. 원문 저작권자가 게재 중단을 요청하면 즉시 삭제합니다.
- **정확성** — AI 요약의 한계로 오류가 있을 수 있습니다. 중요한 내용은 반드시 원문을 직접 확인하세요.
- **광고** — Google AdSense를 통해 디스플레이 광고를 운영합니다. 광고 노출이 콘텐츠 선별 기준에 영향을 주지 않습니다.
- **개인정보** — 이 사이트는 별도의 회원가입이나 개인정보 수집을 하지 않습니다. 방문 통계는 Google Analytics로 집계됩니다.

---

## 데이터 소스

- Anthropic News
- Hugging Face Blog
- Simon Willison's Weblog
- LangChain Blog
- Pinecone Learn
- GitHub Releases (modelcontextprotocol/*, anthropics/*)
- HackerNews (Algolia Search API)

---

## 문의

오류 제보, 다뤄주길 원하는 주제, 기타 문의는 GitHub Issues로 남겨주세요.

→ [github.com/prscsl/llm-mcp-weekly/issues](https://github.com/prscsl/llm-mcp-weekly/issues)

---

*마지막 업데이트: 2026년 4월*

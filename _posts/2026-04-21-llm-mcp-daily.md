---
layout: post
title: "2026-04-21 LLM·MCP 위클리"
date: 2026-04-21 09:00:00 +0900
categories: [weekly]
tags: [ai디자인툴, anthropic, claude, cli, datasette, figma, google apps script, google sheets, llm, opus4.7, tui, 디자인워크플로우, 비용최적화, 실시간데이터, 오픈소스, 터미널, 토크나이저, 토큰카운터, 토큰카운팅]
---

## 2026-04-21 한국어 LLM·MCP 큐레이션

오늘 큐레이션된 항목: 총 **5건**. 
Anthropic, MCP 생태계, HuggingFace, HackerNews 등에서 자동 수집·요약했습니다.

### 도구 / 라이브러리 (3)

#### Claude 토큰 카운터, 모델별 비교 기능 추가

Simon Willison이 공개한 Claude 토큰 카운터 도구에 여러 Claude 모델 간 토큰 수를 비교하는 기능이 추가됐다. 동일한 프롬프트가 모델마다 토크나이징 결과가 달라질 수 있어, 비용 최적화와 컨텍스트 윈도우 관리에 직접적으로 활용할 수 있다. 모델 선택 단계에서 토큰 효율을 미리 검증할 수 있다는 점에서 실무 개발자에게 유용한 도구다.

> HN 199점 · [토론 보기](https://news.ycombinator.com/item?id=47829178)

[원문 보기 →](https://simonwillison.net/2026/Apr/20/claude-token-counts/) (HN (claude))

#### 터미널 UI로 NHL 하키 경기를 실시간으로 보는 Faceoff 도구

Faceoff는 터미널 환경에서 NHL 하키 경기를 실시간으로 추적할 수 있는 TUI(Terminal User Interface) 도구입니다. HN에서 121포인트를 받으며 관심을 끌었으며, CLI 기반 대시보드 제작 방식과 스포츠 데이터 API 활용 사례를 보여줍니다. 터미널 UI 라이브러리나 실시간 데이터 시각화에 관심 있는 한국 개발자에게 참고할 만한 오픈소스 프로젝트입니다.

> HN 121점 · [토론 보기](https://news.ycombinator.com/item?id=47826104)

[원문 보기 →](https://www.vincentgregoire.com/faceoff/) (HN (claude))

#### Claude Opus 4.7, 토크나이저 변경으로 토큰 수 최대 1.5배 증가

Simon Willison이 Claude 토큰 카운터 도구를 업데이트해 여러 모델 간 토큰 수를 비교할 수 있게 했다. Claude Opus 4.7은 최초로 토크나이저를 변경한 모델로, Anthropic 공식 발표에서는 동일 입력 대비 약 1.0~1.35배 토큰 증가를 예고했으나, 실측 결과 Opus 4.7 시스템 프롬프트 기준으로 4.6 대비 1.46배까지 증가한 사례가 확인됐다. Opus 4.7 기반 서비스를 운영하거나 전환을 고려 중인 한국 개발자라면 실제 사용 프롬프트로 토큰 비용을 사전에 검증하는 것이 중요하다.

[원문 보기 →](https://simonwillison.net/2026/Apr/20/claude-token-counts/#atom-everything) (Simon Willison)

### 튜토리얼 / 가이드 (1)

#### Datasette 데이터를 Google Sheets로 가져오는 세 가지 방법

Datasette 인스턴스의 데이터를 Google Sheets에서 직접 조회하는 방법으로 importdata() 함수, 이를 감싼 커스텀 Named Function, 그리고 API 토큰 헤더 전송이 필요한 경우를 위한 Google Apps Script 세 가지 패턴이 소개됩니다. importdata()는 HTTP 헤더 설정을 지원하지 않기 때문에 인증이 필요한 Datasette 엔드포인트에는 Apps Script가 필수입니다. 내부 데이터 분석 도구로 Datasette를 운영 중인 팀이라면, 비개발자도 스프레드시트에서 SQL 조회 결과를 바로 활용할 수 있어 실무 적용 가치가 높습니다.

[원문 보기 →](https://simonwillison.net/2026/Apr/20/datasette-sql/#atom-everything) (Simon Willison)

### 업계 뉴스 (1)

#### Anthropic Claude Design 등장으로 Figma의 위기 가중

Anthropic이 Claude 기반 디자인 도구를 선보이면서 Figma가 기존에 직면한 어려움에 더해 경쟁 압박이 커지고 있다는 분석이 나왔다. AI 네이티브 디자인 툴의 부상이 기존 SaaS 강자들의 시장 지위를 흔드는 흐름이 본격화되는 모습이다. 한국 개발자·디자이너 입장에서는 Figma 의존도를 재검토하고, AI 기반 디자인 워크플로우 전환 시점을 고려해볼 필요가 있다.

> HN 75점 · [토론 보기](https://news.ycombinator.com/item?id=47832366)

[원문 보기 →](https://martinalderson.com/posts/figmas-woes-compound-with-claude-design/) (HN (claude))

---

*본 포스트는 Claude Haiku 4.5로 자동 큐레이션·요약되었습니다. 
각 항목의 저작권은 원저작자에게 있으며, 본 사이트는 한국어 요약과 원문 링크만 제공합니다. 
오류·문의는 [이슈](https://github.com/prscsl/llm-mcp-weekly/issues)로 남겨주세요.*

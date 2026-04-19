---
layout: post
title: "2026-04-20 LLM·MCP 위클리"
date: 2026-04-20 09:00:00 +0900
categories: [weekly]
tags: [ai, ai-에이전트, ai투자, anthropic, api-first, claude, claude code, cli, headless, llm-자동화, llm비용절감, mcp, pycon, python, saas, uber, 개발도구, 단위계, 버그수정, 보안, 브라우저자동화, 성능, 시스템설계, 시스템프롬프트, 에이전트, 에이전틱-엔지니어링, 엔터프라이즈ai]
---

## 2026-04-20 한국어 LLM·MCP 큐레이션

오늘 큐레이션된 항목: 총 **9건**. 
Anthropic, MCP 생태계, HuggingFace, HackerNews 등에서 자동 수집·요약했습니다.

### 릴리스 소식 (2)

#### Claude Code v2.1.114: 에이전트 팀 권한 대화상자 크래시 수정

Claude Code v2.1.114 패치가 릴리스되었다. 이번 업데이트는 에이전트 팀 기능에서 팀원이 도구 사용 권한을 요청할 때 권한 대화상자가 크래시되는 버그를 수정했다. 단일 버그픽스 릴리스이지만, 멀티 에이전트 협업 기능이 실제 사용 환경에서 안정화되고 있음을 보여주는 변경이다. Claude Code의 에이전트 팀 기능을 활용 중인 개발자라면 즉시 업데이트를 권장한다.

[원문 보기 →](https://github.com/anthropics/claude-code/releases/tag/v2.1.114) (GitHub: anthropics/claude-code)

#### Claude Code v2.1.113: 네이티브 바이너리 전환과 보안 강화

Claude Code가 기존 번들 JavaScript 대신 플랫폼별 네이티브 바이너리로 실행 방식을 전환했다. 네트워크 샌드박스에 특정 도메인 차단 설정이 추가되었고, 서브에이전트 무한 대기 방지(10분 타임아웃), Bash 도구의 UI 스푸핑 벡터 차단 등 보안과 안정성이 개선되었다. 멀티라인 입력의 readline 호환, Windows 단축키 지원, 긴 URL 줄바꿈 시 클릭 유지 등 터미널 UX도 다수 보완되어, 일상적으로 Claude Code를 활용하는 개발자라면 즉시 업데이트할 만한 실질적 개선이 담긴 릴리스다.

[원문 보기 →](https://github.com/anthropics/claude-code/releases/tag/v2.1.113) (GitHub: anthropics/claude-code)

### 도구 / 라이브러리 (1)

#### AI Subroutines: 브라우저 작업을 녹화해 토큰 비용 없이 반복 실행하는 자동화 도구

브라우저에서 수행한 작업을 한 번 녹화하면 결정론적 스크립트로 변환해, 이후 LLM 추론 없이 토큰 비용 제로로 반복 실행할 수 있는 도구다. 핵심은 스크립트가 웹페이지 탭 내부에서 직접 실행되어 인증·CSRF·세션 등이 자동으로 유지된다는 점이며, 네트워크 호출과 DOM 조작을 결합해 약 300개 요청 중 핵심 5개만 추출한다. 반복적 브라우저 자동화에서 매번 LLM을 호출하는 비효율을 제거한 접근으로, MCP 서버 연동도 지원해 한국 개발자들의 업무 자동화 파이프라인에 참고할 만하다.

> HN 44점 · [토론 보기](https://news.ycombinator.com/item?id=47810533)

[원문 보기 →](https://www.rtrvr.ai/blog/ai-subroutines-zero-token-deterministic-automation) (HN (mcp server))

### 튜토리얼 / 가이드 (1)

#### 짧은 프롬프트 하나로 블로그 뉴스레터 도구에 새 콘텐츠 유형 추가하기

Simon Willison이 자신의 블로그-뉴스레터 변환 도구에 'beats'라는 새로운 콘텐츠 유형을 추가한 에이전틱 엔지니어링 사례를 소개합니다. 겉보기에 간단한 프롬프트 하나로 상당한 양의 작업을 한 번에 처리한 과정을 보여주며, Datasette에서 데이터를 가져와 Substack 뉴스레터용 HTML로 변환하는 기존 파이프라인을 확장합니다. LLM 에이전트를 활용한 개발 도구 확장의 실전 패턴으로, 자동화 파이프라인을 운영하는 한국 개발자에게 참고할 만한 사례입니다.

[원문 보기 →](https://simonwillison.net/guides/agentic-engineering-patterns/adding-a-new-content-type/#atom-everything) (Simon Willison)

### 업계 뉴스 (2)

#### PyCon US 2026, AI·보안 전용 트랙 신설 — 5월 Long Beach 개최

올해 PyCon US가 5월 13~19일 캘리포니아 롱비치에서 열리며, 처음으로 AI 전용 트랙(금요일)과 보안 전용 트랙(토요일)이 신설되었다. AI 트랙에서는 AI 기반 오픈소스 기여, AI 활용 Python 교육 등 실무 주제가 다뤄지고, Anthropic 소속 Zac Hatfield-Dodds가 트랙 의장으로 참여한다. Python 생태계에서 AI와 보안이 별도 트랙으로 독립할 만큼 비중이 커졌다는 신호로, 한국 Python 개발자도 해당 세션 자료를 주목할 만하다.

[원문 보기 →](https://simonwillison.net/2026/Apr/17/pycon-us-2026/#atom-everything) (Simon Willison)

#### Uber, AI에 3.4조원 투입했지만 CTO가 밝힌 예산 한계

Uber가 AI 도입에 약 34억 달러(약 4.7조 원)를 투입했음에도, CTO가 예산 확보의 어려움을 토로한 것으로 알려졌다. 대규모 기술 기업조차 AI 전환 비용을 감당하기 쉽지 않다는 현실이 드러난 사례다. 한국 기업들도 AI 도입 시 기대 ROI 대비 실제 인프라·운영 비용을 냉정히 산정할 필요가 있음을 시사한다.

> HN 50점 · [토론 보기](https://news.ycombinator.com/item?id=47826328)

[원문 보기 →](https://finance.yahoo.com/sectors/technology/articles/ubers-anthropic-ai-push-hits-223109852.html) (HN (anthropic))

### 연구 / 논문 (1)

#### Claude 시스템 프롬프트 변경 이력을 Git 타임라인으로 추적하기

Anthropic이 공개하는 Claude 채팅용 시스템 프롬프트를 모델별·버전별로 분리한 뒤, 가짜 커밋 날짜를 부여해 GitHub의 커밋 뷰에서 변경 사항을 쉽게 비교할 수 있도록 구성한 프로젝트입니다. 이를 활용해 Opus 4.6과 4.7 간 시스템 프롬프트 차이를 상세히 분석한 노트도 함께 공유되었습니다. LLM 내부 동작 방식을 이해하고 싶은 한국 개발자에게 시스템 프롬프트의 버전별 변화를 추적하는 실용적인 방법을 보여주는 좋은 레퍼런스입니다.

[원문 보기 →](https://simonwillison.net/2026/Apr/18/extract-system-prompts/#atom-everything) (Simon Willison)

### 의견 / 분석 (2)

#### Headless 서비스 시대: AI 에이전트가 UI 대신 API를 쓰는 미래

Matt Webb은 개인 AI가 GUI를 조작하는 것보다 API를 직접 호출하는 headless 방식이 더 빠르고 안정적이라고 주장합니다. Salesforce도 전체 플랫폼을 API·MCP·CLI로 노출하는 'Headless 360'을 발표하며 이 흐름에 합류했습니다. 2010년대 초 API 경제의 부흥기가 AI 에이전트 시대를 맞아 다시 돌아오고 있으며, 기존 SaaS의 사용자 단위 과금 모델에도 큰 변화가 예상됩니다. 한국 개발자에게는 MCP 기반 서비스 연동과 API-first 설계가 점점 더 핵심 역량이 될 것임을 시사합니다.

[원문 보기 →](https://simonwillison.net/2026/Apr/19/headless-everything/#atom-everything) (Simon Willison)

#### 요청 처리량을 SI 단위로 표현하면 어떨까

API나 서버의 요청 처리량(request rate)을 표현할 때 'requests per second' 대신 Hz, mHz, kHz 같은 SI 단위 접두사를 활용하자는 제안을 담은 글이다. 하루 수천 건의 요청이 실제로는 초당 몇 mHz에 불과하다는 식으로 직관적 스케일 비교가 가능해진다. 시스템 설계나 용량 산정 시 단위 환산의 혼란을 줄이고 커뮤니케이션을 명확하게 할 수 있어, 한국 개발자들이 기술 논의에서 참고할 만한 관점이다.

> HN 80점 · [토론 보기](https://news.ycombinator.com/item?id=47790337)

[원문 보기 →](https://entropicthoughts.com/si-units-for-request-rate) (HN (anthropic))

---

*본 포스트는 Claude Haiku 4.5로 자동 큐레이션·요약되었습니다. 
각 항목의 저작권은 원저작자에게 있으며, 본 사이트는 한국어 요약과 원문 링크만 제공합니다. 
오류·문의는 [이슈](https://github.com/prscsl/llm-mcp-weekly/issues)로 남겨주세요.*

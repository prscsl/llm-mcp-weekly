---
layout: post
title: "2026-04-25 LLM·MCP 위클리"
date: 2026-04-25 09:00:00 +0900
categories: [weekly]
tags: [agent-security, agentic engineering, ai투자, anthropic, at protocol, bluesky, chrome extension, claude, claude code, claude-code, cli, codex-cli, credential-management, deepseek, go, google, gpt-5.5, liteparse, llamaindex, llm, llm-품질, mcp, moe, ocr, on-device ai, open-source, openai, pdf파싱, qwen3, rag, rust, simon willison, sqlite, transformers.js, 개발도구, 교육자료, 구독-모델, 뉴스레터, 메시지큐, 시각화, 에이전트 시스템, 오픈웨이트llm, 추천시스템, 포스트모템, 플러그인]
---

## 2026-04-25 한국어 LLM·MCP 큐레이션

오늘 큐레이션된 항목: 총 **16건**. 
Anthropic, MCP 생태계, HuggingFace, HackerNews 등에서 자동 수집·요약했습니다.

### 릴리스 소식 (3)

#### Claude Code v2.1.119: 설정 영속화·멀티 Git 플랫폼·훅 개선

Claude Code v2.1.119에서 /config 설정이 ~/.claude/settings.json에 영속 저장되고 프로젝트·로컬·정책 간 우선순위 체계를 따르게 됐다. --from-pr 옵션이 GitLab MR, Bitbucket PR, GitHub Enterprise URL까지 지원하며, PostToolUse 훅에 duration_ms 필드가 추가돼 도구 실행 시간을 추적할 수 있다. 다양한 Git 호스팅을 쓰는 한국 기업 환경에서 Claude Code 도입 장벽이 낮아진 업데이트다.

[원문 보기 →](https://github.com/anthropics/claude-code/releases/tag/v2.1.119) (GitHub: anthropics/claude-code)

#### DeepSeek V4 프리뷰 공개 — 1.6T 파라미터 오픈웨이트 MoE 모델

DeepSeek이 V4 시리즈 프리뷰로 Pro(1.6T 파라미터, 49B 활성)와 Flash(284B, 13B 활성) 두 모델을 MIT 라이선스로 공개했다. 둘 다 100만 토큰 컨텍스트를 지원하는 MoE 구조이며, Pro는 현존 최대 규모의 오픈웨이트 모델로 Kimi K2.6(1.1T)과 GLM-5.1(754B)을 넘어선다. Flash는 160GB 수준으로 양자화 시 고사양 맥북에서도 로컬 실행 가능성이 있어, 비용 효율적인 자체 호스팅을 고려하는 한국 개발팀에게 실질적인 선택지가 될 수 있다.

[원문 보기 →](https://simonwillison.net/2026/Apr/24/deepseek-v4/#atom-everything) (Simon Willison)

#### llm-openai-via-codex: Codex CLI 인증으로 LLM 도구에서 OpenAI API 호출

Simon Willison이 공개한 llm-openai-via-codex 0.1a0은 OpenAI Codex CLI의 인증 정보를 활용해 LLM 명령줄 도구에서 OpenAI 모델을 호출할 수 있게 해주는 플러그인이다. 별도의 API 키 설정 없이 Codex CLI에 이미 저장된 자격 증명을 재사용하는 방식으로, GPT-5.5 관련 포스트에서 소개된 활용법을 구현한 것이다. 여러 LLM 도구를 병행하는 한국 개발자라면 인증 관리 부담을 줄이는 실용적인 접근법으로 참고할 만하다.

[원문 보기 →](https://simonwillison.net/2026/Apr/23/llm-openai-via-codex/#atom-everything) (Simon Willison)

### 도구 / 라이브러리 (5)

#### Agent Vault — AI 에이전트용 오픈소스 자격증명 프록시

Infisical이 공개한 Agent Vault는 AI 에이전트가 외부 서비스에 접근할 때 필요한 자격증명을 안전하게 중개하는 오픈소스 프록시 겸 볼트다. 에이전트에 직접 API 키나 토큰을 노출하지 않고, 중앙 볼트를 통해 인증을 위임하는 구조로 자격증명 유출 위험을 줄인다. MCP 서버 등 에이전트 도구 생태계가 확장되면서 자격증명 관리가 현실적 과제로 부상하고 있어, 에이전트 기반 워크플로를 설계하는 한국 백엔드 팀에게 참고할 만한 아키텍처 사례다.

> HN 134점 · [토론 보기](https://news.ycombinator.com/item?id=47865822)

[원문 보기 →](https://github.com/Infisical/agent-vault) (HN (mcp server))

#### Agent Vault — AI 에이전트용 오픈소스 자격증명 프록시

Infisical이 공개한 Agent Vault는 AI 에이전트가 외부 서비스에 접근할 때 필요한 자격증명을 안전하게 중개하는 오픈소스 프록시 겸 볼트다. 에이전트에 직접 API 키나 토큰을 노출하지 않고, 중앙 볼트를 통해 인증을 위임하는 구조로 자격증명 유출 위험을 줄인다. MCP 서버 등 에이전트 도구 생태계가 확장되면서 자격증명 관리가 현실적 과제로 부상하고 있어, 에이전트 기반 워크플로를 설계하는 한국 백엔드 팀에게 참고할 만한 아키텍처 사례다.

> HN 134점 · [토론 보기](https://news.ycombinator.com/item?id=47865822)

[원문 보기 →](https://github.com/Infisical/agent-vault) (HN (anthropic))

#### Simon Willison의 밀리초 변환 도구 — LLM 응답 시간 분석용

Simon Willison이 LLM 프롬프트 처리 시간을 밀리초 단위로 보고받을 때 초·분 단위로 빠르게 환산하기 위한 간단한 웹 변환 도구를 만들어 공개했다. 그의 오픈소스 CLI 도구인 LLM(llm.datasette.io)은 프롬프트 실행 시간을 밀리초로 표시하는데, 큰 숫자를 직관적으로 파악하기 어려운 불편을 해소한 것이다. LLM 응답 지연을 모니터링하거나 프롬프트 최적화 작업을 하는 개발자라면 유사한 단위 변환 자동화를 워크플로에 넣어두면 편리하다.

[원문 보기 →](https://simonwillison.net/2026/Apr/24/milliseconds/#atom-everything) (Simon Willison)

#### Honker: SQLite에 Postgres NOTIFY/LISTEN 기능을 추가하는 Rust 확장

SQLite 위에 Postgres 스타일의 NOTIFY/LISTEN 시맨틱을 구현한 Rust 확장 라이브러리가 공개됐다. 큐와 Kafka 스타일 내구성 스트림을 지원하며, Python 등 다양한 언어 바인딩을 제공한다. SQLite 기반 경량 아키텍처를 선호하는 한국 백엔드 개발자라면, Redis나 Kafka 없이도 간단한 비동기 작업 큐와 이벤트 스트림을 구현할 수 있는 실용적인 대안으로 주목할 만하다.

[원문 보기 →](https://simonwillison.net/2026/Apr/24/honker/#atom-everything) (Simon Willison)

#### LiteParse 웹 버전: 브라우저에서 PDF 텍스트 추출

LlamaIndex의 오픈소스 PDF 파싱 도구 LiteParse가 브라우저 환경에서도 동작하도록 포팅되었다. AI 모델 없이 전통적 PDF 파싱과 Tesseract OCR을 조합하며, 다단 레이아웃 등 복잡한 PDF 구조에서도 올바른 텍스트 순서를 복원하는 공간 기반 파싱이 핵심이다. 바운딩 박스 기반 시각적 인용 기능은 RAG 파이프라인에서 답변의 출처를 원문 이미지로 보여줄 수 있어, PDF 기반 Q&A 시스템의 신뢰성을 높이려는 백엔드 개발자에게 실용적인 선택지다.

[원문 보기 →](https://simonwillison.net/2026/Apr/23/liteparse-for-the-web/#atom-everything) (Simon Willison)

### 튜토리얼 / 가이드 (2)

#### LLM 작동 원리를 시각적으로 익히는 인터랙티브 가이드

Andrej Karpathy의 LLM 강의를 기반으로 제작된 인터랙티브 시각 가이드가 공개됐다. 토큰화, 임베딩, 어텐션 메커니즘 등 LLM의 핵심 개념을 단계별로 직접 조작하며 이해할 수 있도록 구성되어 있으며, HN에서 230포인트 이상의 높은 관심을 받았다. 백엔드 엔지니어가 LLM 기반 서비스를 설계할 때 내부 동작 원리를 직관적으로 파악하는 데 유용한 학습 자료다.

> HN 230점 · [토론 보기](https://news.ycombinator.com/item?id=47886517)

[원문 보기 →](https://ynarwal.github.io/how-llms-work/) (HN (claude))

#### Transformers.js로 크롬 확장 프로그램에서 ML 모델 실행하기

Hugging Face의 Transformers.js 라이브러리를 활용해 크롬 확장 프로그램 내에서 직접 머신러닝 추론을 수행하는 방법을 다룬 튜토리얼이다. 서버 없이 브라우저 환경(WebAssembly/WebGPU)에서 텍스트 분류, 번역 등 다양한 모델을 로컬 실행할 수 있어, 사용자 데이터가 외부로 전송되지 않는 프라이버시 이점이 있다. 한국 개발자 입장에서는 별도 백엔드 인프라 없이 LLM 기반 기능을 브라우저 확장에 통합할 수 있는 실용적인 접근법으로, 사내 도구나 생산성 확장 프로그램 개발 시 참고할 만하다.

[원문 보기 →](https://huggingface.co/blog/transformersjs-chrome-extension) (Hugging Face Blog)

### 업계 뉴스 (5)

#### Google, Anthropic에 최대 400억 달러 투자 결정

Google이 Anthropic에 현금과 컴퓨팅 자원을 합산해 최대 400억 달러 규모의 투자를 진행한다. 이는 AI 업계 역대 최대 규모 투자 중 하나로, Google Cloud 인프라와 Anthropic의 모델 개발 역량이 더욱 긴밀하게 연결될 것으로 보인다. Claude API를 활용 중인 한국 개발자라면 Google Cloud 기반 인프라 확장에 따른 서비스 안정성 및 가용 리전 확대 가능성에 주목할 필요가 있다.

> HN 128점 · [토론 보기](https://news.ycombinator.com/item?id=47895080)

[원문 보기 →](https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/) (HN (anthropic))

#### Simon Willison 주간 뉴스레터: GPT-5.5·ChatGPT Images 2.0·Qwen3 정리

Simon Willison이 이번 주 뉴스레터에서 GPT-5.5, ChatGPT Images 2.0, Qwen3-6 27B 등 주요 모델 소식과 함께 블로그 포스트 5건, 링크 8건, 인용 3건을 정리했다. 특히 Agentic Engineering Patterns 가이드의 새 챕터가 추가되어 에이전트 설계 패턴에 관심 있는 개발자라면 참고할 만하다. LLM 생태계 변화를 한눈에 파악하기 좋은 큐레이션으로, 매주 흐름을 놓치고 싶지 않은 백엔드·AI 엔지니어에게 유용하다.

[원문 보기 →](https://simonwillison.net/2026/Apr/24/weekly/#atom-everything) (Simon Willison)

#### Claude Code 품질 저하 원인은 모델이 아닌 하네스 버그 3건이었다

지난 두 달간 Claude Code 품질이 떨어졌다는 불만이 쏟아졌는데, Anthropic 포스트모템에 따르면 모델 자체가 아니라 Claude Code 하네스의 버그 3건이 원인이었다. 특히 1시간 이상 유휴 세션에서 thinking 컨텍스트가 매 턴마다 반복 삭제되어 모델이 건망증 증상을 보인 것이 핵심 문제였다. 에이전트 시스템을 구축하는 한국 개발자라면, 모델 성능 외에도 하네스·오케스트레이션 레이어의 버그가 사용자 경험을 크게 좌우할 수 있다는 점을 설계 시 유의할 필요가 있다.

[원문 보기 →](https://simonwillison.net/2026/Apr/24/recent-claude-code-quality-reports/#atom-everything) (Simon Willison)

#### Bluesky 추천 피드, 거실 PC 한 대로 7만 사용자 서빙하는 아키텍처

Bluesky의 오픈 피드 프로토콜을 활용해 개인이 운영하는 'For You Feed'가 약 7만 2천 명에게 추천 알고리즘을 제공하고 있다. Go + SQLite 단일 프로세스로 90일치 419GB 데이터를 처리하며, 월 30달러(전기료·VPS·도메인)로 운영된다. 분산 소셜 프로토콜에서 개인이 플랫폼급 추천 시스템을 저비용으로 구축할 수 있다는 점은, AT Protocol 기반 서비스를 고려하는 한국 개발자에게 실질적인 아키텍처 레퍼런스가 된다.

[원문 보기 →](https://simonwillison.net/2026/Apr/24/serving-the-for-you-feed/#atom-everything) (Simon Willison)

#### 구글, 앤스로픽에 최대 400억 달러 투자 확대

구글이 앤스로픽에 대한 투자 규모를 최대 400억 달러(약 56조 원)까지 확대하기로 했다. 이는 AI 업계 단일 기업 대상 투자로는 역대 최대 수준이며, 오픈AI에 대한 마이크로소프트의 투자와 직접 경쟁하는 구도다. 한국 개발자 입장에서는 Claude 모델의 인프라·연구 투자가 대폭 늘어나면서 API 성능·안정성 개선과 신규 모델 출시가 가속화될 것으로 기대할 수 있다.

> HN 41점 · [토론 보기](https://news.ycombinator.com/item?id=47894129)

[원문 보기 →](https://www.wsj.com/finance/investing/google-expands-anthropic-investment-with-40-billion-commitment-99b4de74) (HN (anthropic))

### 의견 / 분석 (1)

#### Claude 구독 해지기: 토큰 제한·품질 저하·지원 부재 비판

한 개발자가 Claude 유료 구독을 해지하며 토큰 사용량 제한 문제, 응답 품질의 점진적 하락, 그리고 미흡한 고객 지원 경험을 상세히 공유했다. HN에서 632포인트·378개 댓글을 기록하며 큰 공감을 얻었다. LLM 유료 플랜을 사용하는 한국 개발자라면 토큰 소진 패턴과 품질 변동을 자체적으로 모니터링하고, 단일 모델 종속을 피하는 멀티 모델 전략을 고려할 필요가 있다.

> HN 632점 · [토론 보기](https://news.ycombinator.com/item?id=47892019)

[원문 보기 →](https://nickyreinert.de/en/2026/2026-04-24-claude-critics/) (HN (claude))

---

*본 포스트는 Claude Haiku 4.5로 자동 큐레이션·요약되었습니다. 
각 항목의 저작권은 원저작자에게 있으며, 본 사이트는 한국어 요약과 원문 링크만 제공합니다. 
오류·문의는 [이슈](https://github.com/prscsl/llm-mcp-weekly/issues)로 남겨주세요.*

---
layout: post
title: "2026-04-28 LLM·MCP 위클리"
date: 2026-04-28 09:00:00 +0900
categories: [weekly]
tags: [agi, ai-에이전트, ai안전, ai윤리, ai코딩, ai코딩도구, ai코딩어시스턴트, ai코딩에이전트, ai코딩자동화, chatgpt, checkpoint, codex, google meet, gpt-5.5, langchain, langgraph, llm, openai, openai codex, openai-api, responses api, symphony, toolnode, websocket, 레드팀, 멀티모달, 버그바운티, 식품유통-자동화, 실시간 번역, 업무자동화, 에이전트, 에이전트 자동화, 엔터프라이즈ai, 오케스트레이션, 오픈소스, 워크스페이스에이전트, 음성 합성, 이미지생성, 플러그인]
---

## 2026-04-28 한국어 LLM·MCP 큐레이션

오늘 큐레이션된 항목: 총 **17건**. 
Anthropic, MCP 생태계, HuggingFace, HackerNews 등에서 자동 수집·요약했습니다.

### 릴리스 소식 (5)

#### OpenAI Symphony: 이슈 트래커를 AI 에이전트 시스템으로 바꾸는 오픈소스 오케스트레이션 스펙

OpenAI가 Codex 에이전트 오케스트레이션을 위한 오픈소스 명세 Symphony를 공개했다. GitHub Issues 같은 이슈 트래커를 진입점으로 삼아 에이전트가 상시 작업을 수행하도록 설계되었으며, 엔지니어의 컨텍스트 스위칭 부담을 줄이고 개발 생산성을 높이는 것이 목표다. 기존 CI/CD 파이프라인에 에이전트 계층을 얹는 구조여서, MCP 기반 워크플로를 구축 중인 한국 백엔드팀이라면 자동화 범위를 넓히는 참고 아키텍처로 살펴볼 만하다.

[원문 보기 →](https://openai.com/index/open-source-codex-orchestration-symphony) (OpenAI Blog)

#### OpenAI, GPT-5.5 공개 — 코딩·리서치·데이터 분석 강화 모델

OpenAI가 차세대 모델 GPT-5.5를 발표했다. 코딩, 리서치, 데이터 분석 등 복잡한 작업에서 속도와 성능을 동시에 개선한 것이 특징이며, 다양한 도구를 연계한 멀티태스크 처리 능력을 강조하고 있다. 한국 개발자 입장에서는 API 기반 코딩 에이전트나 데이터 파이프라인 자동화 워크플로에 어떤 실질적 성능 차이가 있는지, 가격 정책과 함께 기존 GPT-4o 대비 마이그레이션 가치를 따져볼 시점이다.

[원문 보기 →](https://openai.com/index/introducing-gpt-5-5) (OpenAI Blog)

#### ChatGPT 이미지 생성 2.0 — 텍스트 렌더링·다국어·시각 추론 대폭 개선

OpenAI가 ChatGPT에 탑재되는 차세대 이미지 생성 모델을 공개했다. 텍스트 렌더링 정확도가 크게 향상되었고, 다국어 입력을 지원하며, 고급 시각 추론 기능이 추가되어 프롬프트 의도를 더 정밀하게 반영한다. 한국어 프롬프트 지원이 포함되어 있어 국내 개발자들이 UI 목업, 다이어그램, 마케팅 이미지 등을 별도 번역 없이 생성할 수 있다는 점이 실무적으로 의미 있다.

[원문 보기 →](https://openai.com/index/introducing-chatgpt-images-2-0) (OpenAI Blog)

#### LangGraph prebuilt 1.0.12 — ToolNode 상태 복원 버그 수정

LangGraph prebuilt 1.0.12가 릴리스되었다. 이번 업데이트의 핵심은 ToolNode가 Pregel 헬퍼를 통해 채널에서 상태를 올바르게 복원(hydrate)하도록 수정한 것이다. 함께 langgraph 1.1.10과 checkpoint 4.0.3도 배포되었다. LangGraph 기반 에이전트에서 ToolNode를 활용해 복잡한 도구 호출 흐름을 구성하는 경우, 상태 관리 안정성이 개선되므로 업그레이드를 검토할 만하다.

[원문 보기 →](https://github.com/langchain-ai/langgraph/releases/tag/prebuilt%3D%3D1.0.12) (GitHub: langchain-ai/langgraph)

#### LangGraph Checkpoint 4.0.3 — JSON 역직렬화 버그 수정

LangGraph의 체크포인트 라이브러리 4.0.3이 릴리스되었다. 핵심 수정 사항은 lc=2 형식의 JSON blob을 allowlist 없이도 안전한 타입에 한해 복원할 수 있도록 한 것으로, 기존 체크포인트 데이터 로딩 시 발생하던 역직렬화 오류를 해결한다. 아울러 중복 경고 메시지 정리와 langsmith 의존성이 0.7.31로 업데이트되었다. LangGraph 기반 에이전트를 운영 중이라면 체크포인트 복원 안정성 향상을 위해 업그레이드를 권장한다.

[원문 보기 →](https://github.com/langchain-ai/langgraph/releases/tag/checkpoint%3D%3D4.0.3) (GitHub: langchain-ai/langgraph)

### 튜토리얼 / 가이드 (7)

#### OpenAI Codex 시작 가이드: 프로젝트 설정부터 첫 태스크까지

OpenAI가 Codex 활용을 위한 단계별 입문 가이드를 공개했다. 프로젝트 초기 설정, 스레드 생성, 첫 번째 태스크 완료까지의 과정을 순서대로 안내하며, AI 코딩 에이전트를 처음 접하는 개발자도 빠르게 워크플로우에 통합할 수 있도록 구성되어 있다. 국내 개발자들이 Codex를 실무 코드 리뷰나 리팩토링 보조 도구로 도입할 때 참고할 만한 공식 출발점이다.

[원문 보기 →](https://openai.com/academy/codex-how-to-start) (OpenAI Blog)

#### OpenAI Codex 개요 — 챗봇을 넘어 작업 자동화 도구로

OpenAI Codex는 단순 대화형 AI를 넘어 외부 도구 연동, 문서·대시보드 등 실제 산출물 생성, 반복 작업 자동화까지 수행하는 에이전트형 코딩 도구다. 채팅 인터페이스에서 코드 생성만 하던 기존 방식과 달리 워크플로 전체를 연결하는 방향으로 진화했다. 한국 개발자 입장에서는 MCP 기반 도구 연동 흐름과 맞닿아 있어, 사내 자동화 파이프라인 설계 시 Codex의 도구 통합 패턴을 참고할 만하다.

[원문 보기 →](https://openai.com/academy/what-is-codex) (OpenAI Blog)

#### OpenAI Codex 실무 활용 사례 10가지 정리

OpenAI가 Codex를 업무 환경에서 활용하는 대표적인 방법 10가지를 소개했다. 파일·워크플로우·다양한 도구를 연결해 반복 작업 자동화, 산출물 생성, 입력 데이터를 결과물로 변환하는 실용적 시나리오를 다룬다. 코드 생성뿐 아니라 문서 작성, 데이터 정리 등 비개발 업무까지 포괄하는 점이 특징이다. 국내 개발팀에서도 CI/CD 스크립트 생성이나 보일러플레이트 자동화 등 일상 업무에 바로 적용해볼 만한 힌트가 담겨 있다.

[원문 보기 →](https://openai.com/academy/top-10-use-cases-codex-for-work) (OpenAI Blog)

#### OpenAI Codex 플러그인·스킬 활용법: 도구 연결과 워크플로 자동화

OpenAI Codex에서 플러그인과 스킬 기능을 활용해 외부 도구 연결, 데이터 접근, 반복 워크플로 자동화를 구현하는 방법을 다룬다. 플러그인은 Codex의 기능을 확장해 다양한 서비스와 통합할 수 있게 하며, 스킬은 자주 사용하는 작업 패턴을 재사용 가능한 형태로 정의한다. 국내 개발자들이 코드 생성 에이전트를 실무에 도입할 때 단순 코드 완성을 넘어 CI/CD, DB 조회 등 기존 도구 체인과 연동하는 구체적 패턴을 참고할 수 있다.

[원문 보기 →](https://openai.com/academy/codex-plugins-and-skills) (OpenAI Blog)

#### OpenAI Codex 실전 활용 가이드: 워크스페이스 설정부터 태스크 완료까지

OpenAI가 Codex 도구의 단계별 활용 가이드를 공개했다. 워크스페이스 초기 설정, 스레드·프로젝트 생성, 파일 관리, 태스크 실행까지의 전체 워크플로를 다룬다. AI 코딩 어시스턴트를 업무에 도입하려는 한국 개발자에게 Codex의 프로젝트 단위 작업 관리 방식은 기존 단일 프롬프트 방식과 차별화되는 점이므로, 팀 단위 도입 전 워크플로 설계 참고 자료로 활용할 만하다.

[원문 보기 →](https://openai.com/academy/working-with-codex) (OpenAI Blog)

#### ChatGPT 워크스페이스 에이전트로 팀 업무 자동화하기

OpenAI가 ChatGPT 내에서 반복 업무를 자동화하는 워크스페이스 에이전트의 구축·활용·확장 방법을 안내하는 교육 콘텐츠를 공개했다. 외부 도구 연동과 팀 단위 운영 효율화에 초점을 맞추며, 에이전트가 단순 챗봇을 넘어 실무 워크플로우에 통합되는 구체적 패턴을 다룬다. 사내 업무 자동화나 ChatGPT Enterprise·Team 플랜 도입을 검토하는 한국 개발팀이라면 에이전트 설계 시 참고할 만한 실용적 가이드다.

[원문 보기 →](https://openai.com/academy/workspace-agents) (OpenAI Blog)

#### OpenAI Responses API에 WebSocket 도입 — 에이전트 워크플로 지연 줄이기

OpenAI가 Responses API에 WebSocket 연결과 커넥션 범위 캐싱을 도입하여 에이전트 루프의 API 오버헤드를 줄이고 모델 응답 지연을 개선한 방법을 Codex 에이전트 사례로 설명했다. 반복적으로 API를 호출하는 에이전트 패턴에서 매 요청마다 HTTP 핸드셰이크와 컨텍스트 재전송이 발생하는 비효율을 WebSocket 지속 연결로 해소하는 접근이다. 국내에서도 LLM 기반 코딩 에이전트나 자동화 파이프라인을 구축할 때, 호출 지연이 사용자 경험에 직접 영향을 주므로 동일한 최적화 전략을 검토할 필요가 있다.

[원문 보기 →](https://openai.com/index/speeding-up-agentic-workflows-with-websockets) (OpenAI Blog)

### 업계 뉴스 (4)

#### Google Meet 실시간 음성 번역, 모바일로 확대

Google Meet의 실시간 음성 번역 기능이 모바일 기기로 확대 배포되고 있다. 두 사람이 서로 다른 언어로 대화하면 Meet가 원래 화자의 음색을 모방해 상대 언어로 변환·재생하는 방식이다. 현재 영어·스페인어·프랑스어·독일어·포르투갈어·이탈리아어 6개 언어만 지원되며, 웹 브라우저에서는 작동하지만 iOS 기기 간 연결은 아직 불안정한 알파 단계로 보고된다. 한국어 지원 시점은 미정이나, 음성 합성·번역 모델의 실시간 파이프라인 구현 사례로서 LLM 기반 다국어 서비스를 설계하는 개발자에게 참고할 만하다.

[원문 보기 →](https://simonwillison.net/2026/Apr/27/speech-translation-in-google-meet-is-now-rolling-out-to-mobile-d/#atom-everything) (Simon Willison)

#### Choco, OpenAI API 기반 AI 에이전트로 식품 유통 자동화 사례

식품 유통 플랫폼 Choco가 OpenAI API를 활용해 주문 처리, 재고 관리 등 유통 워크플로우를 AI 에이전트로 자동화하여 생산성을 높이고 사업 성장을 이끌어낸 사례다. 기존 수작업 중심의 식품 공급망에 LLM 기반 에이전트를 도입해 실질적인 업무 효율 개선을 달성했다는 점이 핵심이다. 국내 유통·물류 도메인에서 AI 에이전트 도입을 검토하는 엔지니어에게 아키텍처 설계와 적용 범위의 참고 사례가 될 수 있다.

[원문 보기 →](https://openai.com/index/choco) (OpenAI Blog)

#### OpenAI, GPT-5.5 생물안전 버그바운티 프로그램 공개

OpenAI가 GPT-5.5 모델의 생물 안전(biosafety) 관련 취약점을 찾는 레드팀 챌린지를 시작했다. 참가자가 생물 위험 정보에 대한 범용 탈옥(universal jailbreak)을 발견하면 최대 2만 5천 달러의 보상금을 지급한다. AI 안전 연구 커뮤니티와 외부 전문가를 동시에 활용해 모델 출시 전 위험을 선제적으로 차단하려는 접근으로, 국내에서도 AI 안전 평가 체계를 설계할 때 참고할 만한 사례다.

[원문 보기 →](https://openai.com/index/gpt-5-5-bio-bug-bounty) (OpenAI Blog)

#### OpenAI Codex, 엔터프라이즈 확장 본격화 — Codex Labs 출범

OpenAI가 Codex Labs를 새롭게 출범하고 Accenture, PwC, Infosys 등 글로벌 SI·컨설팅 기업과 파트너십을 맺어 기업 환경에서의 Codex 도입을 본격 지원한다. 주간 활성 사용자(WAU)가 400만 명을 돌파했으며, 소프트웨어 개발 전 주기에 걸쳐 Codex를 활용할 수 있도록 확장하는 데 초점을 두고 있다. 국내 SI·엔터프라이즈 개발 조직에서도 AI 코딩 도구 도입 전략을 구체화할 시점이며, 대형 컨설팅사 주도의 엔터프라이즈 배포 모델이 어떤 형태로 국내에 유입될지 주목할 필요가 있다.

[원문 보기 →](https://openai.com/index/scaling-codex-to-enterprises-worldwide) (OpenAI Blog)

### 의견 / 분석 (1)

#### OpenAI, AGI 개발 5대 원칙 공개

OpenAI CEO 샘 알트먼이 조직의 AGI 개발을 이끄는 다섯 가지 핵심 원칙을 공식 발표했다. 이 원칙들은 AGI가 전 인류에게 혜택을 줄 수 있도록 하겠다는 미션 아래, 안전성·투명성·책임감 등 OpenAI의 방향성을 구체화한 내용이다. 한국 개발자 입장에서는 OpenAI API 정책이나 모델 출시 기조에 이 원칙이 어떻게 반영될지 주시할 필요가 있다.

[원문 보기 →](https://openai.com/index/our-principles) (OpenAI Blog)

---

*본 포스트는 Claude Haiku 4.5로 자동 큐레이션·요약되었습니다. 
각 항목의 저작권은 원저작자에게 있으며, 본 사이트는 한국어 요약과 원문 링크만 제공합니다. 
오류·문의는 [이슈](https://github.com/prscsl/llm-mcp-weekly/issues)로 남겨주세요.*

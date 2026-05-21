---
layout: post
title: "2026-05-13 LLM·MCP 위클리"
date: 2026-05-13 09:00:00 +0900
categories: [weekly]
tags: [ai, ai 개발, ai 에이전트, ai-ethics, api 업데이트, automation, aws, checkpointsqlite, cli, codex, datasette, generative-ai, langchain, langgraph, llm, mitchell hashimoto, nvidia, openai, postgresql, redis, tiktok, tui, yc 스타트업, 개발, 개발도구, 금융, 기술 트렌드, 데이터 통합, 도구, 도구 호출, 라이브러리 업데이트, 모델 최적화, 버전 업데이트, 보안, 분석 도구, 브라우저 앱, 상태 기계, 업데이트, 오픈ai, 의존성 변경, 자바스크립트, 정부 기술, 체크포인트, 코드 품질, 클라우드, 클론 프로젝트, 테스트]
---

## 2026-05-13 한국어 LLM·MCP 큐레이션

오늘 큐레이션된 항목: 총 **20건**. 
Anthropic, MCP 생태계, HuggingFace, HackerNews 등에서 자동 수집·요약했습니다.

### 릴리스 소식 (10)
{: .cat-section .cat-release}

#### agentic OpenGravity 프로젝트 공개

제로 설치로 실행 가능한 앤티그라비티 클론 프로젝트인 오픈그라비티가 발표되었습니다. 자바스크립트로 구현된 이 프로젝트는 사용자 경험을 최적화한 브라우저 기반 애플리케이션입니다. 한국 개발자에게는 브라우저 기반 애플리케이션 개발에 대한 새로운 접근 방식을 제시합니다.

> HN 100점 · [토론 보기](https://news.ycombinator.com/item?id=48100192)

[원문 보기 →](https://github.com/ab-613/opengravity) (HN (agentic))

#### datasette 1.0a29 업데이트: 테스트 안정성 개선

datasette 1.0a29 버전이 공개되었습니다. 주요 변경사항은 TokenRestrictions.abbreviated() 유틸리티 메서드 추가, 테이블 헤더 표시 개선, 모바일 브라우저 버그 수정 등입니다. 한국 개발자에게는 테스트 환경의 안정성을 높이는 기능이 유용합니다.

[원문 보기 →](https://simonwillison.net/2026/May/12/datasette/#atom-everything) (Simon Willison)

#### LLM 0.32a2 업데이트: OpenAI 모델 추론 툴 사용

LLM 0.32a2 업데이트에서 OpenAI 모델이 /v1/responses 엔드포인트를 사용하게 되면서 추론 과정을 시각화할 수 있게 되었습니다. 이는 개발자가 모델의 사고 과정을 확인하고, -R 플래그로 숨길 수 있습니다. 한국 개발자에게는 모델의 내부 로직 분석에 유용합니다.

[원문 보기 →](https://simonwillison.net/2026/May/12/llm/#atom-everything) (Simon Willison)

#### cline CLI cli-v3.0.0 릴리스, TUI 업데이트

cline CLI cli-v3.0.0이 출시되어 새 SDK 기반의 TUI가 도입되었습니다. 한국 개발자에게는 CLI 도구의 사용 편의성 향상과 현지화 지원을 기대할 수 있습니다.

[원문 보기 →](https://github.com/cline/cline/releases/tag/cli-v3.0.0) (GitHub: cline/cline)

#### langgraph 1.2.0 업데이트: 오류 처리 및 상태 관리 개선

langgraph 1.2.0이 출시되어 오류 처리 기능이 강화되고 상태 그래프 관리가 개선되었습니다. 이 업데이트는 분산 시스템에서의 안정성과 복구성을 높이는 데 기여합니다. 한국 개발자에게는 작업 중단 시 데이터 복구 기능이 유용합니다.

[원문 보기 →](https://github.com/langchain-ai/langgraph/releases/tag/1.2.0) (GitHub: langchain-ai/langgraph)

#### langgraph 1.1.0 릴리스: 업데이트 및 의존성 변경

langchain-ai/langgraph에서 1.1.0 버전이 공개되었습니다. 주요 변경사항은 alpha 패키지 업데이트, urllib3 및 langchain-core 의존성 버전 변경, SQLite 체크포인트 기능 개선입니다. 한국 개발자에게는 라이브러리 호환성과 성능 최적화에 도움이 될 수 있습니다.

[원문 보기 →](https://github.com/langchain-ai/langgraph/releases/tag/prebuilt%3D%3D1.1.0) (GitHub: langchain-ai/langgraph)

#### langgraph CLI 0.4.26 업데이트: 프리릴리스 API 지원 추가

langchain-ai/langgraph CLI 0.4.26이 발간되었습니다. 주요 변경사항으로는 프리릴리스 API 버전 지원 추가, 의존성 라이브러리 업데이트 등이 포함됩니다. 한국 개발자에게는 새로운 API 기능을 통해 기존 기능의 확장성과 유연성이 향상될 수 있습니다.

[원문 보기 →](https://github.com/langchain-ai/langgraph/releases/tag/cli%3D%3D0.4.26) (GitHub: langchain-ai/langgraph)

#### langgraph checkpointsqlite 3.1.0 릴리스

langchain-ai의 langgraph에서 checkpointsqlite 3.1.0이 공식 출시되었습니다. 이 업데이트는 alpha 패키지의 정식 버전으로 전환하고, 의존성 라이브러리 업데이트 및 기능 개선을 포함합니다. 한국 개발자에게는 작업 흐름 최적화와 호환성 향상이 기대됩니다.

[원문 보기 →](https://github.com/langchain-ai/langgraph/releases/tag/checkpointsqlite%3D%3D3.1.0) (GitHub: langchain-ai/langgraph)

#### langgraph checkpointpostgres 3.1.0 릴리스

langchain-ai의 langgraph에서 checkpointpostgres 3.1.0이 공식 출시되었습니다. 주요 변경사항으로는 alpha 패키지 업데이트, 의존성 버전 변경, 시드 블롭 브랜치에 컬럼 별칭 추가 등이 포함됩니다. 한국 개발자에게는 데이터 처리 효율성 향상과 호환성 개선이 주요 이점입니다.

[원문 보기 →](https://github.com/langchain-ai/langgraph/releases/tag/checkpointpostgres%3D%3D3.1.0) (GitHub: langchain-ai/langgraph)

#### langgraph 4.1.0 릴리스: 체크포인트 개선 및 문서 업데이트

langgraph 4.1.0이 출시되어 체크포인트 관련 기능이 업데이트되었습니다. 주요 변경사항으로는 알파 버전 패키지를 정식 버전으로 변경하고, 라이브러리 의존성을 업데이트하여 안정성을 높였습니다. 한국 개발자에게는 체크포인트 관리 및 데尔타 채널 기능 개선으로 작업 효율성이 향상될 수 있습니다.

[원문 보기 →](https://github.com/langchain-ai/langgraph/releases/tag/checkpoint%3D%3D4.1.0) (GitHub: langchain-ai/langgraph)

### 도구 / 라이브러리 (2)
{: .cat-section .cat-tool}

#### Gemini 도구 호출을 26M 모델로 압축한 Needle 프로젝트

Gemini의 도구 호출 기능을 26M 파라미터 모델로 압축해 개발자 경험 개선. 한국 개발자에게는 대규모 모델 대체용으로 활용 가능. LLM 최적화 및 효율적인 API 호출 전략 고려 필요.

> HN 241점 · [토론 보기](https://news.ycombinator.com/item?id=48111896)

[원문 보기 →](https://github.com/cactus-compute/needle) (HN (agentic))

#### Statewright: 시각화 상태 기계로 AI 에이전트 신뢰성 확보

Statewright은 AI 에이전트의 신뢰성을 높이기 위한 시각화 상태 기계 도구입니다. 상태 전환 로직을 시각적으로 설계하고 관리할 수 있어, 복잡한 로직을 명확하게 표현할 수 있습니다. 한국 개발자에게는 AI 에이전트 개발 시 상태 기계 설계에 유용한 도구로 활용할 수 있습니다.

> HN 63점 · [토론 보기](https://news.ycombinator.com/item?id=48108778)

[원문 보기 →](https://github.com/statewright/statewright) (HN (model context protocol))

### 업계 뉴스 (6)
{: .cat-section .cat-news}

#### claude AWS 플랫폼 공개

클라우드 AI 플랫폼이 AWS에 공식 출시되었습니다. 개발자들은 클라우드 기반 AI 서비스를 쉽게 구축할 수 있는 새로운 도구를 제공합니다. 한국 개발자에게는 클라우드 인프라 최적화와 확장성 향상이 기대됩니다.

> HN 218점 · [토론 보기](https://news.ycombinator.com/item?id=48103042)

[원문 보기 →](https://claude.com/blog/claude-platform-on-aws) (HN (claude))

#### ICE 에이전트, Palantir 통해 2천만 명 데이터 보유

미국 연방수사국(ICE) 에이전트들이 Palantir 기술을 활용해 약 2천만 명의 개인 정보를 저장하고 있다고 보도되었다. 이는 대규모 데이터 통합 및 분석 기능을 제공하는 Palantir의 플랫폼이 정부 기관에 활용되고 있음을 보여주는 사례다. 한국 개발자에게는 데이터 통합 및 보안 기술의 중요성을 다시 일깨워주는 사례로 볼 수 있다.

> HN 69점 · [토론 보기](https://news.ycombinator.com/item?id=48107743)

[원문 보기 →](https://www.404media.co/ice-agents-have-list-of-20-million-people-on-their-iphones-thanks-to-palantir/) (HN (agentic))

#### AI 에이전트 분석 도구 'Voker' 출시 소식

AI 에이전트 분석 플랫폼 'Voker'가 YC S24 스타트업으로서 출시되었습니다. 한국 개발자에게는 AI 에이전트의 성능을 체계적으로 모니터링하고 최적화할 수 있는 기회가 될 수 있습니다. 이 도구는 AI 에이전트 개발의 효율성을 높이는 데 기여할 수 있습니다.

> HN 35점 · [토론 보기](https://news.ycombinator.com/item?id=48109962)

[원문 보기 →](https://voker.ai) (HN (anthropic))

#### 금융 팀이 Codex를 활용한 실무 사례

OpenAI의 Codex를 활용해 금융 팀이 MBR, 보고서 팩, 변동성 브릿지 등을 구축하는 방안을 소개합니다. 한국 개발자에게는 AI 기반 자동화 도구의 실무 적용 사례로 참고할 수 있습니다.

[원문 보기 →](https://openai.com/academy/how-finance-teams-use-codex) (OpenAI Blog)

#### NVIDIA, Codex와 GPT-5.5로 생산성 시스템 구축

NVIDIA 연구진이 Codex와 GPT-5.5를 활용해 실제 시스템 구축 및 연구 아이디어 실행 실험에 성공했습니다. 한국 개발자에게는 AI 기반 자동화 도구의 실제 적용 사례를 제공하며, 생산성 향상에 기여할 수 있는 방향성을 제시합니다.

[원문 보기 →](https://openai.com/index/nvidia) (OpenAI Blog)

#### 오픈AI, 자동차 중고차 플랫폼 AutoScout24 AI 개발 협력

오픈AI가 자동차 중고차 플랫폼 AutoScout24에 Codex와 ChatGPT를 도입해 개발 주기 단축과 코드 품질 향상에 성공했다. 한국 개발자에게는 AI 기반 개발 도구의 실무 적용 사례로 참고할 수 있다. AI 기술이 소프트웨어 개발에 미치는 영향을 파악하는 데 유용한 사례로 평가된다.

[원문 보기 →](https://openai.com/index/autoscout24) (OpenAI Blog)

### 의견 / 분석 (2)
{: .cat-section .cat-opinion}

#### Simon Willison 업데이트

Mo Bitar의 AI 실무자 대상 경고 글에서 자동화 전략과 윤리적 고려가 중요하다고 강조합니다. 한국 개발자에게는 기술적 실력 외에도 조직 내에서의 전략적 커뮤니케이션 능력이 필요합니다. 자동화 도입 시 기존 팀원의 역할 변화에 대한 명확한 전략이 필요하며, 이는 조직 내에서의 윤리적 책임을 다하는 데 기여합니다.

[원문 보기 →](https://simonwillison.net/2026/May/12/mo-bitar/#atom-everything) (Simon Willison)

#### Mitchell Hashimoto, 기술 결정자들의 동기와 트렌드 추종 현실 지적

Mitchell Hashimoto가 기술 결정자들이 경영진의 압박에 따라 트렌드를 따르는 현실을 지적했습니다. 한국 개발자에게는 기술 선택 시 경영 전략과 시장 동향을 고려하는 것이 중요합니다. 기술 트렌드를 이해하고 적절히 활용하는 것이 성공적인 프로젝트 설계에 핵심입니다.

[원문 보기 →](https://simonwillison.net/2026/May/12/mitchell-hashimoto/#atom-everything) (Simon Willison)

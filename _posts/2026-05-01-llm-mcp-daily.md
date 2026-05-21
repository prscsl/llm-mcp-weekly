---
layout: post
title: "2026-05-01 LLM·MCP 위클리"
date: 2026-05-01 09:00:00 +0900
categories: [weekly]
tags: [ai, ai 에이전트, ai 윤리, anthropic, anthropic-sdk-python, claude, claude-code, cma, codex, gemini, generative-ai, google, grok, llm, llms, mcp, postgres, qwen, rust, tag, unix 스타일, v0.102.0, v0.103.0, v0.103.1, 개발, 개발 생산성, 개발도구, 개발자 도구, 구글, 기술 연습, 대규모 모델, 도구, 디지털 전환, 로그 관리, 모델 선택, 모델 업데이트, 법률, 비트코인, 샌드박스, 서버 플랫폼, 소상공인, 안전성, 암호 해독, 업데이트, 에이전트, 오토리페어, 오픈소스, 인수, 코드 에이전트, 코드 작성, 코드검색, 코드베이스, 클라우드, 테스트 도구, 토큰효율, 하드웨어 최적화, 협약]
---

## 2026-05-01 한국어 LLM·MCP 큐레이션

오늘 큐레이션된 항목: 총 **30건**. 
Anthropic, MCP 생태계, HuggingFace, HackerNews 등에서 자동 수집·요약했습니다.

### 릴리스 소식 (10)
{: .cat-section .cat-release}

#### claude-code v2.1.146 업데이트 주요 변경 사항

claude-code v2.1.146이 발표되었습니다. 주요 변경으로는 코드 검토 명령어 이름 변경, Windows PowerShell 오류 수정, MCP 관련 버그 수정 등이 포함됩니다. 한국 개발자에게는 Windows 환경에서의 안정성 향상과 자동 업데이트 문제 해결이 주요 이점입니다.

[원문 보기 →](https://github.com/anthropics/claude-code/releases/tag/v2.1.146) (GitHub: anthropics/claude-code)

#### claude-code v2.1.145 업데이트: 개발자 편의성 강화

claude-code v2.1.145이 공개되었습니다. JSON 형식으로 라이브 세션을 표시하고, OTEL 스팬에 agnet_id 추가 등 개발자 편의 기능이 강화되었습니다. 한국 개발자에게는 스크립팅과 상태 모니터링에 유용한 기능이 추가되었습니다.

[원문 보기 →](https://github.com/anthropics/claude-code/releases/tag/v2.1.145) (GitHub: anthropics/claude-code)

#### claude-code v2.1.144 업데이트: 백그라운드 세션 개선 및 버그 수정

claude-code v2.1.144이 발표되었습니다. 백그라운드 세션 지원, 타임라인 표시, 플러그인 업데이트 정보 등 다양한 기능 개선과 버그 수정이 포함되었습니다. 한국 개발자에게는 VS Code에서의 터미널 안정성 향상과 macOS 백그라운드 세션 문제 해결이 주요 이점입니다.

[원문 보기 →](https://github.com/anthropics/claude-code/releases/tag/v2.1.144) (GitHub: anthropics/claude-code)

#### claude-code v2.1.143 업데이트 주요 변경사항

claude-code v2.1.143이 출시되었습니다. 플러그인 의존 관리, 컨텍스트 비용 예측, PowerShell 실행 정책 변경 등 주요 기능 개선이 포함되었습니다. 한국 개발자에게는 작업 트리 설정 및 배경 세션 유지 기능이 유용합니다.

[원문 보기 →](https://github.com/anthropics/claude-code/releases/tag/v2.1.143) (GitHub: anthropics/claude-code)

#### claude-code v2.1.142 업데이트: 개발자 편의성 강화

claude-code v2.1.142이 새 기능과 버그 수정으로 개선되었습니다. 개발자에게는 작업 트리 인식 및 빠른 모드 최적화 등 편의성이 높아졌습니다. 특히 macOS에서의 안정성 향상과 브라우저 세션 처리 개선으로 생산성 향상이 기대됩니다.

[원문 보기 →](https://github.com/anthropics/claude-code/releases/tag/v2.1.142) (GitHub: anthropics/claude-code)

#### claude-code v2.1.141 업데이트: 개발자 편의성 강화

claude-code v2.1.141이 공개되었습니다. 주요 변경사항으로는 터미널 시퀀스 필드 추가, HTTPS 대신 SSH를 사용하는 GitHub 플러그인 복제 옵션, 작업 공간 ID 환경 변수 등이 포함됩니다. 이 업데이트는 개발자들이 작업 환경을 더욱 유연하게 조절할 수 있도록 지원합니다.

[원문 보기 →](https://github.com/anthropics/claude-code/releases/tag/v2.1.141) (GitHub: anthropics/claude-code)

#### anthropic-sdk-python v0.103.1 릴리스

anthropic-sdk-python v0.103.1이 2026년 5월 19일 출시되었습니다. 주요 변경사항은 러너 관련 버그 수정입니다. 세션 도구 러너의 소유권 문제 해결로 인해 시스템 안정성이 개선되었습니다.

[원문 보기 →](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.103.1) (GitHub: anthropics/anthropic-sdk-python)

#### anthropic-sdk-python v0.103.0 릴리스: CMA에서 자체 호스팅 샌드박스 지원 추가

anthropic-sdk-python v0.103.0이 출시되었습니다. CMA에서 자체 호스팅 샌드박스 지원을 추가하여 개발자가 로컬 환경에서 안전하게 모델 테스트를 수행할 수 있도록 했습니다.

[원문 보기 →](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.103.0) (GitHub: anthropics/anthropic-sdk-python)

#### anthropic-sdk-python v0.102.0 릴리스

anthropic-sdk-python v0.102.0이 2026년 5월 13일 출시되었습니다. 주요 기능으로는 베타 기능을 위한 타입 추가, 캐시 진단 지원, 파이던틱 이터레이터 검증 기능이 포함되었습니다.

[원문 보기 →](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.102.0) (GitHub: anthropics/anthropic-sdk-python)

#### llm-gemini 0.32 업데이트: Gemini 3.5 Flash 모델 추가

llm-gemini 0.32 버전이 발표되어 Gemini 3.5 Flash 모델이 추가되었습니다. 이 업데이트는 빠른 추론 속도와 효율적인 메모리 사용을 제공하며, 한국 개발자들이 대규모 언어 모델을 활용한 애플리케이션 개발에 유용할 수 있습니다.

[원문 보기 →](https://simonwillison.net/2026/May/19/llm-gemini-2/#atom-everything) (Simon Willison)

### 도구 / 라이브러리 (9)
{: .cat-section .cat-tool}

#### Claude 기반 코드 및 Codex 기술 연습 도구 출시

DrCatHicks가 개발한 학습 기회 제공 플랫폼에서 Claude 기반 코드 작성 및 Codex 기술 연습 도구가 출시되었습니다. 이 도구는 실수를 줄이고 효율적인 기술 습득을 지원합니다. HN에서 253개의 추천과 50개의 댓글을 받았습니다.

> HN 253점 · [토론 보기](https://news.ycombinator.com/item?id=48130679)

[원문 보기 →](https://github.com/DrCatHicks/learning-opportunities) (HN (claude))

#### 코드 검색 효율성 98% 향상한 Semble 도구 공개

Semble는 grep 대비 토큰 사용량 98% 감소를 기록한 코드 검색 도구로, 개발자 생산성 향상에 기여할 수 있는 잠재력을 보여줍니다. 한국 개발자에게는 대규모 코드베이스 관리 시 토큰 효율성의 중요성이 높아 이 도구의 활용 가치가 큽니다.

> HN 441점 · [토론 보기](https://news.ycombinator.com/item?id=48169874)

[원문 보기 →](https://github.com/MinishLab/semble) (HN (mcp server))

#### Claude 법률 분석 도구 한국 개발자에게 필요한 정보

Claude 법률 분석 도구가 법률 전문가와 개발자 간 협업을 용이하게 합니다. 한국 개발자에게는 법률 문서 자동화 및 분석 기능이 기존 작업 흐름에 통합 가능성을 제시합니다. 이 도구는 법률 분야의 AI 활용 확대에 기여할 수 있습니다.

> HN 225점 · [토론 보기](https://news.ycombinator.com/item?id=48141234)

[원문 보기 →](https://github.com/anthropics/claude-for-legal) (HN (claude))

#### Rust로 만든 Unix 스타일 코드 에이전트 Zerostack

Zerostack은 Rust로 개발된 Unix 스타일의 코드 에이전트로, 개발자 경험을 향상시킬 수 있는 새로운 도구입니다. 이 도구는 Rust 생태계에서 주목받고 있으며, 한국 개발자에게도 유용한 기능을 제공할 수 있습니다.

> HN 571점 · [토론 보기](https://news.ycombinator.com/item?id=48164287)

[원문 보기 →](https://crates.io/crates/zerostack/1.0.0) (HN (agentic))

#### 로컬 LLM 선택 가이드: 하드웨어에 최적화된 모델 비교

하드웨어 성능에 따라 최적화된 로컬 LLM 모델을 비교한 가이드입니다. 한국 개발자에게는 자원 제약 환경에서 효율적인 모델 선택 전략을 제공합니다. 하드웨어 사양에 맞는 모델을 선택해 성능 최적화를 추구해야 합니다.

> HN 283점 · [토론 보기](https://news.ycombinator.com/item?id=48146369)

[원문 보기 →](https://github.com/Andyyyy64/whichllm) (HN (local llm))

#### Superlog, 자체 설치 및 오류 수정 기능 탑재한 Observability 솔루션 출시

Superlog는 자동 설치 및 자동 오류 수정 기능을 갖춘 Observability 솔루션으로, 개발자에게 실시간 모니터링과 문제 해결을 지원합니다. 한국 개발자에게는 기존의 수동 설정 과정을 줄여 생산성을 높일 수 있는 혁신적인 솔루션입니다.

> HN 70점 · [토론 보기](https://news.ycombinator.com/item?id=48195021)

[원문 보기 →](https://superlog.sh/) (HN (mcp server))

#### mcp server 프로젝트 공개

인스포지는 코드 에이전트를 위한 오픈소스 서버 플랫폼으로, Heroku와 유사한 기능을 제공합니다. 한국 개발자에게는 클라우드 기반의 코드 실행 환경을 제공하여 개발 생산성을 높일 수 있는 기회입니다.

> HN 60점 · [토론 보기](https://news.ycombinator.com/item?id=48181342)

[원문 보기 →](https://github.com/InsForge/InsForge) (HN (mcp server))

#### 아르덴트, Postgres 샌드박스 1초 생성

아르덴트는 Postgres 데이터베이스를 쉽게 테스트할 수 있는 샌드박스 환경을 제공합니다. 개발자는 데이터베이스 설정을 복잡하게 하지 않고도 빠르게 테스트를 진행할 수 있어 생산성 향상에 기여합니다. 이 도구는 클라우드 기반의 실시간 테스트 환경을 제공하여 개발자 경험을 개선합니다.

> HN 98점 · [토론 보기](https://news.ycombinator.com/item?id=48124436)

[원문 보기 →](https://www.tryardent.com/) (HN (coding agent))

#### 10 tokens per second 실제 속도 비교

Mike Veerman의 HTML 앱을 통해 LLM 모델의 토큰 처리 속도를 시뮬레이션해 보여줍니다. 10토큰/초의 실제 성능을 이해하는 데 도움이 됩니다. 한국 개발자에게는 모델 성능 평가 기준을 참고할 수 있는 자료입니다.

[원문 보기 →](https://simonwillison.net/2026/May/20/tokens-per-second/#atom-everything) (Simon Willison)

### 업계 뉴스 (9)
{: .cat-section .cat-news}

#### claude Small 업데이트

Anthropic이 소상공인을 위한 AI 기반 도구 '클라우드'를 발표했습니다. 이 도구는 고객 관리, 마케팅, 재무 분석 등 다양한 업무를 자동화할 수 있습니다. 한국 개발자에게는 AI 기술의 실용적 적용 사례를 제공하며, 소규모 비즈니스의 디지털 전환을 지원하는 데 기여할 수 있습니다.

> HN 540점 · [토론 보기](https://news.ycombinator.com/item?id=48130950)

[원문 보기 →](https://www.anthropic.com/news/claude-for-small-business) (HN (claude))

#### claude Bitcoin 업데이트

11년 전 잃어버린 비트코인 지갑 암호를 AI 기반 암호 해독 도구로 복구한 사례입니다. 한국 개발자에게는 AI 기술의 암호 해독 가능성과 보안 취약점 분석에 대한 시사점을 제공합니다.

> HN 332점 · [토론 보기](https://news.ycombinator.com/item?id=48136240)

[원문 보기 →](https://www.tomshardware.com/tech-industry/cryptocurrency/bitcoin-trader-recovers-usd400-000-using-claude-ai-after-losing-wallet-password-11-years-ago-bot-tried-3-5-trillion-passwords-before-decrypting-an-old-wallet-backup) (HN (claude))

#### Karpathy, Anthropic에 합류해 LLM 분야 주목

Karpathy가 Anthropic에 합류해 대규모 언어 모델 분야에서 주목받고 있다. 이는 기술 혁신과 연구 개발에 대한 강한 의지를 보여주는 신호로, 한국 개발자들에게도 기술적 영감을 주고 있다. 이 소식은 AI 연구 및 개발 분야에서 중요한 변화를 예고한다.

> HN 1406점 · [토론 보기](https://news.ycombinator.com/item?id=48194352)

[원문 보기 →](https://twitter.com/karpathy/status/2056753169888334312) (HN (anthropic))

#### Anthropic, Stainless 인수로 AI 개발 혁신 가속화

Anthropic이 Stainless를 인수하며 AI 개발 분야의 혁신을 가속화하고 있습니다. 이 인수를 통해 기업용 AI 솔루션과 개발자 도구를 강화할 수 있게 되었습니다. 한국 개발자에게는 새로운 기술 기회와 협업 가능성의 확대가 기대됩니다.

> HN 527점 · [토론 보기](https://news.ycombinator.com/item?id=48182281)

[원문 보기 →](https://www.anthropic.com/news/anthropic-acquires-stainless) (HN (anthropic))

#### Qwen3.7-Max, 에이전트 기술 혁신 발표

Qwen3.7-Max는 에이전트 기술 분야에서 중요한 진보를 이루었습니다. 이 업데이트는 개발자들이 더 복잡한 작업을 처리할 수 있는 능력을 제공합니다. 한국 개발자에게는 이 기술이 자동화 및 효율성 향상에 기여할 수 있는 잠재력을 보여줍니다.

> HN 637점 · [토론 보기](https://news.ycombinator.com/item?id=48205626)

[원문 보기 →](https://qwen.ai/blog?id=qwen3.7) (HN (agentic))

#### Anthropic, 게이츠 기금과 2억 달러 협약 발표

AI 기업 Anthropic이 게이츠 기금과 2억 달러 규모의 협약을 발표했습니다. 이 협약은 안전한 AI 개발과 윤리적 기준 마련을 목표로 합니다. 한국 개발자에게는 AI 윤리 기준 마련과 기술 혁신의 균형을 고려한 정책 방향을 보여주는 사례로 의미가 있습니다.

> HN 121점 · [토론 보기](https://news.ycombinator.com/item?id=48136662)

[원문 보기 →](https://www.anthropic.com/news/gates-foundation-partnership) (HN (anthropic))

#### SpaceX, Anthropic과 클라우드 서비스 협약 체결

SpaceX가 Anthropic과 클라우드 컴퓨팅 자원 공유 협약을 맺고, 월 12억 달러를 받는 것으로 알려졌습니다. 이는 대규모 AI 모델 개발에 필요한 자원 확보를 위한 전략으로, 한국 개발자에게도 클라우드 인프라 최적화 전략을 참고할 수 있는 사례입니다.

[원문 보기 →](https://simonwillison.net/2026/May/20/spacex-s1/#atom-everything) (Simon Willison)

#### 구글 I/O 2026, Gemini Spark 및 Antigravity 발표 분석

구글 I/O 2026에서 발표된 Gemini Spark는 사용자 맞춤형 AI 에이전트로, Gmail, 드라이브 등 구글 앱과 원활하게 연동됩니다. Antigravity는 개발자 도구로, CLI 도구와 SDK를 통해 다양한 플랫폼에서 활용 가능합니다. 한국 개발자에게는 새로운 AI 기반 애플리케이션 개발 기회가 열릴 수 있습니다.

[원문 보기 →](https://simonwillison.net/2026/May/20/google-io/#atom-everything) (Simon Willison)

#### 구글, Gemini 3.5 Flash 출시 및 사용 확대 발표

구글이 Gemini 3.5 Flash를 공식 출시하며, 검색, 개발자 플랫폼, 기업용 솔루션 등 다양한 분야에 적용 중입니다. 한국 개발자에게는 Google AI Studio 및 Android Studio에서의 지원이 주목할 만한 점입니다.

[원문 보기 →](https://simonwillison.net/2026/May/19/gemini-35-flash/#atom-everything) (Simon Willison)

### 연구 / 논문 (2)
{: .cat-section .cat-research}

#### claude How 업데이트

클라우드 코드가 대규모 코드베이스에서 어떻게 작동하는지 설명하며, 개발자에게 실용적인 팁을 제공합니다. 한국 개발자에게는 클라우드 기반 개발 환경의 효율성 향상 전략을 제시합니다.

> HN 247점 · [토론 보기](https://news.ycombinator.com/item?id=48144494)

[원문 보기 →](https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start) (HN (claude))

#### Forge: 대규모 모델의 안전성 강화 기술

Forge는 8B 모델의 안전성 수준을 53%에서 99%로 높이는 기술입니다. 한국 개발자에게는 대규모 모델의 안전성 확보에 대한 새로운 접근 방식을 제시합니다. 이 기술은 AI 시스템의 신뢰성을 높이는 데 기여할 수 있습니다.

> HN 646점 · [토론 보기](https://news.ycombinator.com/item?id=48192383)

[원문 보기 →](https://github.com/antoinezambelli/forge) (HN (agentic))

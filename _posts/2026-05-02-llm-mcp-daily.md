---
layout: post
title: "2026-05-02 LLM·MCP 위클리"
date: 2026-05-02 09:00:00 +0900
categories: [weekly]
tags: [agent-definitions, ai, ai 연구, ai 인프라, ai 프로그래밍, ai 하드웨어, ai-agents, ai코드생성, atom-everything, bun, csp, css, datasette, five, gemini, goose, i/o 2026, inaturalist, ip 제한, ipo, julia-evans, linux, llm, llms, minutes, months, react native, rust, simon, six, 개발자, 개발자 도구, 구글, 기술 경제, 기술 선택, 기술 트렌드, 데이터 수집, 데이터 처리, 도구, 도시 생태, 동물관찰, 드론, 릴리스, 모델 최적화, 버그 수정, 보안, 샌드박스, 생성형 ai, 서버 보안, 업데이트, 오픈소스, 의료, 이름 변경, 자동화, 자연, 자연사진, 정부 정책, 취업 전략, 코드, 코드 생성, 코드 품질, 코딩에이전트, 클라우드, 파인튜닝, 프로젝트, 프로젝트 역사, 프리트레인링, 형식 검증, 환경]
---

## 2026-05-02 한국어 LLM·MCP 큐레이션

오늘 큐레이션된 항목: 총 **30건**. 
Anthropic, MCP 생태계, HuggingFace, HackerNews 등에서 자동 수집·요약했습니다.

### 릴리스 소식 (8)
{: .cat-section .cat-release}

#### datasette-llm-accountant 0.1a4 버전 업데이트

datasette-llm-accountant 0.1a4 버전이 출시되었습니다. 이 업데이트는 응답 체인 추적 버그를 수정하여 시스템의 안정성을 높였습니다. 한국 개발자에게는 데이터베이스와 LLM 통합 개발 시 오류 추적에 유용한 변경 사항입니다.

[원문 보기 →](https://simonwillison.net/2026/May/19/datasette-llm-accountant/#atom-everything) (Simon Willison)

#### llm-gemini 0.32a0 업데이트: 토큰 스트리밍 기능 추가

llm-gemini 0.32a0 버전이 출시되었습니다. 새로운 버전은 llm 0.32a0 이상과 호환되며, 추론 토큰을 스트리밍할 수 있는 기능을 추가했습니다. 이 기능은 실시간으로 모델의 사고 과정을 확인할 수 있어, 개발자들이 모델의 동작을 더 잘 이해하고 최적화할 수 있는 기회를 제공합니다.

[원문 보기 →](https://simonwillison.net/2026/May/19/llm-gemini/#atom-everything) (Simon Willison)

#### datasette-llm 0.1a8 버전 업데이트

datasette-llm 0.1a8 버전이 출시되었습니다. llm_prompt_context() 훅의 버그 수정으로 응답 체인 수집이 개선되었습니다. 이 업데이트는 데이터셋과 LLM 통합 개발에 유용합니다.

[원문 보기 →](https://simonwillison.net/2026/May/19/datasette-llm/#atom-everything) (Simon Willison)

#### inaturalist-clumper 0.1 버전 출시

iNaturalist 관찰 기록을 블로그에 게시하기 위한 인프라 중 하나로, 실제 운영 환경에서 사용하며 개선 사항을 반영한 0.1 버전을 공개했습니다. 한국 개발자에게는 데이터 처리 및 API 활용 사례로 참고할 수 있습니다.

[원문 보기 →](https://simonwillison.net/2026/May/15/inaturalist-clumper/#atom-everything) (Simon Willison)

#### datasette-llm-limits 0.1a0 버전 출시

Simon Willison이 개발한 datasette-llm-limits 플러그인 0.1a0 버전이 공개되었습니다. 이 플러그인은 datasette-llm과 datasette-llm-accountant와 연동해 사용자별 또는 글로벌 LLM 사용량 제한을 설정할 수 있도록 합니다. 사용량 관리 설정 예시는 제공되었습니다.

[원문 보기 →](https://simonwillison.net/2026/May/15/datasette-llm-limits/#atom-everything) (Simon Willison)

#### datasette-ip-rate-limit 0.1a0 릴리스, 한국 개발자에게 필요한 정보

Simon Willison이 datasette-ip-rate-limit 0.1a0를 발표하며, 불량 크롤러로 인한 서버 과부하를 방지하기 위해 IP 제한 기능을 추가했습니다. 이 플러그인은 특정 경로에 대한 요청을 제한해 서버 부하를 줄이는 데 효과적입니다. 한국 개발자에게는 웹 애플리케이션 보안 및 성능 최적화에 대한 참고 자료가 됩니다.

[원문 보기 →](https://simonwillison.net/2026/May/14/datasette-ip-rate-limit/#atom-everything) (Simon Willison)

#### goose v1.34.1 릴리스: 우분투 22.04 기반 빌드 지원

goose v1.34.1이 우분투 22.04 기반으로 비- vulkan Linux 버전을 빌드 지원을 추가했습니다. 이 업데이트는 다양한 환경에서의 호환성을 높이고, 개발자들이 더 유연한 배포 옵션을 제공합니다. 한국 개발자에게는 기존 시스템과의 호환성 향상으로 인해 작업 효율이 증가할 수 있습니다.

[원문 보기 →](https://github.com/aaif-goose/goose/releases/tag/v1.34.1) (GitHub: block/goose)

#### goose v1.34.0 업데이트: 개발자 중심 기능 강화

goose v1.34.0이 출시되어 Hooks 지원, ACP 호환성, Linux Vulkan 지원 등 개발자 편의 기능이 업데이트되었습니다. 한국 개발자에게는 ACP 통합과 커스터마이징 기능이 실제 개발 환경에서 유용하게 활용될 수 있습니다.

[원문 보기 →](https://github.com/aaif-goose/goose/releases/tag/v1.34.0) (GitHub: block/goose)

### 도구 / 라이브러리 (2)
{: .cat-section .cat-tool}

#### Simon Willison 업데이트

Simon Willison이 개발한 QR 코드 생성기 도구를 소개합니다. 텍스트, URL, WiFi 연결 정보를 QR 코드로 생성할 수 있으며, 사용자 친화적인 인터페이스와 다양한 설정 옵션을 제공합니다. 한국 개발자에게는 웹 애플리케이션 개발 시 QR 코드 생성 기능을 구현하는 데 참고할 수 있는 사례입니다.

[원문 보기 →](https://simonwillison.net/2026/May/15/qr-code-generator/#atom-everything) (Simon Willison)

#### CSP 허용 목록 실험 도구 소개

CSP 보호된 샌드박스 iframe에서 앱을 로드하고, 커스텀 fetch()로 CSP 오류를 캡처해 부모 창에 전달하는 실험 도구입니다. 한국 개발자에게는 보안 검토 및 동적 허용 목록 관리에 유용한 사례로 분석됩니다.

[원문 보기 →](https://simonwillison.net/2026/May/13/csp-allow/#atom-everything) (Simon Willison)

### 업계 뉴스 (11)
{: .cat-section .cat-news}

#### Simon Willison, 5분 동안 LLM 6개월 동향 발표

Simon Willison이 PyCon US 2026에서 발표한 5분 동안의 LLM 6개월 동향 요약 자료입니다. 지난 6개월 동안의 주요 변화를 정리한 발표 자료입니다.

[원문 보기 →](https://simonwillison.net/2026/May/19/5-minute-llms/#atom-everything) (Simon Willison)

#### GDS, NHS의 오픈소스 철수 결정에 대한 입장을 발표

영국 정부 디지털 서비스(GDS)가 NHS의 오픈소스 접근 철수 결정에 대한 입장을 발표했습니다. 공개 소스 코드를 기본으로 유지하고, 비공개로 전환할 때는 신중하게 접근해야 한다는 권고를 내렸습니다. 이는 공공 부문에서 소프트웨어 개발 방식에 큰 영향을 미칠 수 있습니다. 한국 개발자에게는 오픈소스의 장단점을 재조명하는 계기가 될 수 있습니다.

[원문 보기 →](https://simonwillison.net/2026/May/17/gds-weighs-in/#atom-everything) (Simon Willison)

#### simonwillison.net에서 서부 가물치와 바위 날개 pigeon 관찰 기록 발표

simonwillison.net의 Simon Willison이 2026년 5월 15일, 미국 캘리포니아 지역에서 서부 가물치와 바위 날개 pigeon을 관찰한 내용을 공유합니다. 이는 자연 생태계와 도시 환경의 상호작용을 보여주는 사례로, 개발자에게는 생태계 보호와 기술의 역할에 대한 고민을 제기합니다.

[원문 보기 →](https://simonwillison.net/2026/May/15/sighting-361818285/#atom-everything) (Simon Willison)

#### Datasette 블로그 시작, 개발자에게 새로운 소식

Datasette 프로젝트가 공식 블로그를 시작했습니다. OpenAI Codex를 사용해 블로그를 만들었고, 개발자들에게 새로운 기능과 정보를 제공할 예정입니다. 이는 AI 기반 개발 도구의 활용 사례로, 한국 개발자에게도 참고할 만한 내용입니다.

[원문 보기 →](https://simonwillison.net/2026/May/13/welcome-to-the-datasette-blog/#atom-everything) (Simon Willison)

#### Railway, 코드 생성 에이전트로 개발자 혁명 이끌다

Railway가 300만 명의 사용자와 주간 10만 명의 신규 가입자를 기록하며 코드 생성 에이전트를 중심으로 서비스를 확장하고 있습니다. 한국 개발자에게는 자동화 도구로 인한 생산성 향상과 협업 방식 변화를 경험할 수 있는 기회입니다.

[원문 보기 →](https://www.latent.space/p/railway) (Latent Space)

#### 구글 I/O 2026, Gemini 3.5 Flash 등 신기술 발표

구글이 2026년 I/O 컨퍼런스에서 Gemini 3.5 Flash, Omni(비디오용 NanoBanana), Spark(백그라운드 에이전트), Antigravity 2.0 등 신기술을 발표했습니다. 한국 개발자에게는 실시간 처리 및 멀티모달 기능 강화로 AI 앱 개발의 효율성과 유연성이 높아질 것으로 기대됩니다.

[원문 보기 →](https://www.latent.space/p/ainews-google-io-2026-gemini-35-flash) (Latent Space)

#### Cerebras 600억 IPO, 한국 개발자에게 어떤 영향?

Cerebras가 600억 달러 규모의 IPO를 발표하며 AI 하드웨어 분야에서 주목받고 있다. 이는 대규모 AI 모델 개발에 필요한 하드웨어 인프라 확대에 기여할 것으로 기대된다. 한국 개발자에게는 고성능 컴퓨팅 자원 접근성 향상과 기술 경쟁력 강화에 기회가 될 수 있다.

[원문 보기 →](https://www.latent.space/p/ainews-cerebras-60b-ipo-slowly-then) (Latent Space)

#### Latent Space에서 Everything is Conductor 발표

AI 기반의 새로운 기술이 모든 분야에서 변화를 일으키고 있습니다. 이 트렌드는 기존 기술과의 융합을 통해 새로운 가능성을 열어가고 있으며, 특히 한국 개발자에게는 기술 혁신에 적응하는 전략을 고려해야 합니다.

[원문 보기 →](https://www.latent.space/p/ainews-everything-is-conductor) (Latent Space)

#### AI-Native 의료 혁신, 100M 의사 진료 방문 및 10–20시간 절약

Abridge가 환자와 의료진의 대화를 의료 시스템의 핵심으로 전환하며, AI-Native 기반의 진료 프로세스 최적화를 실현하고 있습니다. 한국 개발자에게는 의료 데이터 처리 및 자동화 기술의 새로운 가능성을 제시합니다.

[원문 보기 →](https://www.latent.space/p/abridge) (Latent Space)

#### Latent Space 업데이트

주요 코딩 에이전트의 장기적 추세를 보여주는 조용한 날입니다. 한국 개발자에게는 AI 코드 생성 도구의 경쟁이 심화되고 있어 기술적 차별화가 중요합니다.

[원문 보기 →](https://www.latent.space/p/ainews-codex-rises-claude-meters) (Latent Space)

#### AINews-파인튜닝의 종말, LLM 개발자에게 어떤 영향?

최근 파인튜닝 기술의 발전이 둔화되고 있는 것으로 보입니다. 이는 대규모 언어 모델의 성능 향상에 대한 기대를 재조명하게 합니다. 한국 개발자에게는 모델 최적화 전략을 재검토할 필요가 있습니다.

[원문 보기 →](https://www.latent.space/p/ainews-the-end-of-finetuning) (Latent Space)

### 연구 / 논문 (5)
{: .cat-section .cat-research}

#### coding agent 업데이트

AI 코드 루프의 안정성과 신뢰성을 높이기 위한 형식 검증 게이트 기술이 제안되었다. 이 기술은 코드의 동작을 수학적으로 보장하여 버그를 사전에 방지할 수 있다. 한국 개발자에게는 복잡한 시스템에서 안정적인 코드 작성을 지원할 수 있는 기술로 주목받고 있다.

> HN 115점 · [토론 보기](https://news.ycombinator.com/item?id=48209323)

[원문 보기 →](https://reubenbrooks.dev/blog/structural-backpressure-beats-smarter-agents/) (HN (coding agent))

#### 시몬 윌리슨, 로스앤젤레스 강에서 Glaucous-winged Gull, Brown Pelican, Snowy Egret, Canada Goose 관찰 기록

미국 로스앤젤레스 강에서 Glaucous-winged Gull, Brown Pelican, Snowy Egret, Canada Goose 등 다양한 조류를 관찰한 사진입니다. 한국 개발자에게는 자연 사진의 기술적 측면과 데이터 수집 방식에 대한 참고가 될 수 있습니다.

[원문 보기 →](https://simonwillison.net/2026/May/18/sighting-362781627/#atom-everything) (Simon Willison)

#### 오픈클라우 이름 변경: Warelay → OpenClaw

Simon Willison이 발표한 내용에 따르면, OpenClaw은 2025년 11월부터 이름을 여러 번 변경하며 현재의 이름으로 발전했습니다. 이는 프로젝트의 목표와 기능 변화를 반영합니다. 한국 개발자에게는 프로젝트의 역사와 변화를 이해하는 데 도움이 됩니다.

[원문 보기 →](https://simonwillison.net/2026/May/16/openclaw-names/#atom-everything) (Simon Willison)

#### Latent Space 업데이트

최신 AI 트렌드를 반영한 전방위 연구소 취업 전략을 공유합니다. 기술 트렌드를 정확히 파악하고, 실무 경험과 연구 역량을 결합해 경쟁력을 높일 수 있습니다. 한국 개발자에게는 AI 기술의 발전 속도를 따라가며 전문성과 실무 능력을 동시에 강화하는 기회로 활용할 수 있습니다.

[원문 보기 →](https://www.latent.space/p/ainews-how-to-land-a-job-at-a-frontier) (Latent Space)

#### Latent Space 업데이트

우크라이나 드론 창업자 Yaroslav Azhnyuk이 AI 지도 드론 무기로 전환한 경로를 분석합니다. 서방의 대응이 느려지고 있다는 경고를 담고 있습니다. 한국 개발자에게는 드론 기술의 경제성과 자동화 기술 발전 방향을 참고할 수 있습니다.

[원문 보기 →](https://www.latent.space/p/the-fourth-law) (Latent Space)

### 의견 / 분석 (4)
{: .cat-section .cat-opinion}

#### Julia Evans, CSS 기술에 대한 진지한 접근

Julia Evans가 CSS의 어려움을 인정하며 기술을 진지하게 다룬 경험을 공유합니다. CSS는 복잡한 문제를 해결하려는 노력이 반영된 기술로, 개발자들이 적절한 접근법을 통해 효율적으로 활용할 수 있습니다. 이는 한국 개발자들에게도 CSS 구조화에 대한 새로운 시각을 제공합니다.

[원문 보기 →](https://simonwillison.net/2026/May/16/julia-evans/#atom-everything) (Simon Willison)

#### Simon Willison 업데이트

React Native로의 이동이 언어 고정을 해제하는 사례로, 기존 앱을 유지하면서도 유연한 전략을 선택한 사례입니다. 한국 개발자에게는 기술 선택의 유연성과 유지보수 비용 절감의 균형을 보여주는 사례로 주목할 만합니다.

[원문 보기 →](https://simonwillison.net/2026/May/14/not-so-locked-in/#atom-everything) (Simon Willison)

#### Mitchell Hashimoto, Bun 프로젝트에서 Zig에서 Rust로의 이식 언급

Mitchell Hashimoto가 Bun 프로젝트에서 Zig에서 Rust로의 이식을 언급하며, 프로그래밍 언어의 유연성에 대해 강조했습니다. 이는 언어 선택의 유연성이 중요하다는 점을 보여줍니다. 한국 개발자에게는 다양한 언어 선택이 가능하다는 점에서 유용한 정보입니다.

[원문 보기 →](https://simonwillison.net/2026/May/14/mitchell-hashimoto/#atom-everything) (Simon Willison)

#### Boris Mann, '11 AI 에이전트' 표현 의미 없어

Boris Mann이 '11 AI 에이전트'라는 표현은 의미가 없다고 지적했습니다. 이는 단순히 수량을 세는 것이 아니라, 실제 작업에 어떻게 활용되는지가 중요하다는 의미입니다. 한국 개발자에게는 이처럼 수치 중심의 표현이 실제 기술적 가치를 반영하지 못하는 문제를 인식할 수 있는 계기가 됩니다.

[원문 보기 →](https://simonwillison.net/2026/May/13/boris-mann/#atom-everything) (Simon Willison)

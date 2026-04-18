---
layout: post
title: "2026-04-18 LLM·MCP 위클리"
date: 2026-04-18 09:00:00 +0900
categories: [weekly]
tags: [ai-에이전트, ai정책, anthropic, bugfix, claude code, datasette, llm-보안, llm에이전트, mcp, nvidia, ocr, python, spice, sqlite, 강화학습, 미국정부ai, 이커머스ai, 취약점-자동탐지, 하드웨어 자동화, 합성데이터]
---

## 2026-04-18 한국어 LLM·MCP 큐레이션

오늘 큐레이션된 항목: 총 **7건**. 
Anthropic, MCP 생태계, HuggingFace, HackerNews 등에서 자동 수집·요약했습니다.

### 릴리스 소식 (1)

#### Datasette 1.0a28 — 알파27 호환성 버그 긴급 수정

Datasette 1.0a27에서 발생한 execute_write_fn() 콜백 파라미터명 호환성 버그 등 여러 문제를 긴급 수정한 알파28이 릴리스되었다. database.close()가 쓰기 연결까지 종료하도록 개선되었고, datasette.close() 메서드가 새로 추가되어 서버 종료 시 모든 리소스를 자동 정리한다. pytest 플러그인도 포함되어 테스트 중 임시 인스턴스의 파일 디스크립터 누수를 방지한다. Datasette 플러그인을 개발하거나 운영 중인 한국 개발자라면 a27을 건너뛰고 a28로 직접 업그레이드하는 것이 안전하다.

[원문 보기 →](https://simonwillison.net/2026/Apr/17/datasette/#atom-everything) (Simon Willison)

### 도구 / 라이브러리 (2)

#### Claude Code로 SPICE 시뮬레이션부터 오실로스코프 검증까지 자동화

SPICE 회로 시뮬레이션 결과를 실제 오실로스코프(LeCroy)로 측정한 데이터와 자동 비교·검증하는 워크플로를 Claude Code와 MCP를 활용해 구현한 사례다. 시뮬레이션 실행, 장비 제어, 파형 비교까지의 과정을 LLM이 오케스트레이션하는 구조로, HN에서 115포인트를 기록하며 주목받았다. 하드웨어 엔지니어링 영역에서도 MCP 기반 도구 연동이 실질적 생산성 향상으로 이어질 수 있음을 보여주는 흥미로운 데모다.

> HN 115점 · [토론 보기](https://news.ycombinator.com/item?id=47801255)

[원문 보기 →](https://lucasgerads.com/blog/lecroy-mcp-spice-demo/) (HN (claude))

#### Claude Code로 SPICE 시뮬레이션부터 오실로스코프 검증까지 자동화

SPICE 회로 시뮬레이션 결과를 실제 오실로스코프(LeCroy)로 측정한 데이터와 자동 비교·검증하는 워크플로를 Claude Code와 MCP를 활용해 구현한 사례다. 시뮬레이션 실행, 장비 제어, 파형 비교까지의 과정을 LLM이 오케스트레이션하는 구조로, HN에서 115포인트를 기록하며 주목받았다. 하드웨어 엔지니어링 영역에서도 MCP 기반 도구 연동이 실질적 생산성 향상으로 이어질 수 있음을 보여주는 흥미로운 데모다.

> HN 115점 · [토론 보기](https://news.ycombinator.com/item?id=47801255)

[원문 보기 →](https://lucasgerads.com/blog/lecroy-mcp-spice-demo/) (HN (mcp server))

### 업계 뉴스 (1)

#### 미 백악관, 연방기관에 Anthropic Mythos 모델 접근권 부여

블룸버그 보도에 따르면 미국 백악관이 연방 정부 기관들에 Anthropic의 Mythos 모델 접근 권한을 제공할 예정이다. 이는 미국 정부가 AI 기술을 공공 부문에 본격 도입하려는 움직임의 일환으로, Anthropic이 정부 시장에서 입지를 강화하고 있음을 보여준다. 한국 개발자 관점에서는 미국 공공 부문 AI 도입 가속화가 글로벌 AI 규제·조달 기준에 영향을 미칠 수 있어 주목할 만하다.

> HN 32점 · [토론 보기](https://news.ycombinator.com/item?id=47798006)

[원문 보기 →](https://www.reuters.com/technology/white-house-give-us-agencies-anthropic-mythos-access-bloomberg-news-reports-2026-04-16/) (HN (anthropic))

### 연구 / 논문 (3)

#### Anthropic Mythos 연구를 공개 모델로 재현한 보안 실험 결과

Vidoc Security 팀이 Anthropic의 Mythos 연구(LLM의 보안 취약점 자율 발견·악용 능력 평가)를 공개 모델로 재현하는 데 성공했다. 비공개 내부 모델이 아닌 누구나 접근 가능한 모델에서도 유사한 결과가 나왔다는 점이 핵심이다. 한국 개발자 입장에서 LLM 기반 보안 도구의 가능성과 함께, AI 에이전트가 코드베이스 취약점을 자동 탐지하는 시대가 가까워지고 있음을 시사한다.

> HN 99점 · [토론 보기](https://news.ycombinator.com/item?id=47806116)

[원문 보기 →](https://blog.vidocsecurity.com/blog/we-reproduced-anthropics-mythos-findings-with-public-models) (HN (anthropic))

#### NVIDIA Nemotron OCR v2: 합성 데이터 기반 다국어 OCR 모델 공개

NVIDIA가 합성 데이터 파이프라인으로 학습한 다국어 OCR 모델 Nemotron OCR v2를 공개했다. FOTS 아키텍처 기반으로 텍스트 감지·인식·관계 모델링을 단일 네트워크에 통합하며, A100 GPU 기준 34.7 pages/s로 PaddleOCR v5 대비 28배 이상 빠른 추론 속도를 달성했다. 한국어·중국어·일본어 등 CJK 언어는 단어 경계 문제를 고려해 줄 단위 인식 방식을 채택했으며, 한국어 벤치마크에서 NED 0.047로 경쟁 모델을 크게 앞섰다. 한국어 합성 데이터만 227만 건이 포함된 학습 데이터셋도 CC-BY-4.0으로 함께 공개되어, 국내 문서 OCR 파이프라인 구축 시 파인튜닝 베이스라인으로 활용할 수 있다.

[원문 보기 →](https://huggingface.co/blog/nvidia/nemotron-ocr-v2) (Hugging Face Blog)

#### Ecom-RLVE: 이커머스 대화형 AI를 검증 가능한 강화학습으로 훈련하는 프레임워크

이커머스 챗봇이 자연스럽게 대화는 하지만 실제 장바구니 담기, 교환·반품 처리 같은 복잡한 작업은 제대로 수행하지 못하는 문제를 해결하기 위해, 8가지 쇼핑 시나리오별 검증 환경과 12축 난이도 커리큘럼을 갖춘 강화학습 프레임워크가 공개되었다. LLM 평가자 없이 코드로 보상을 산출하며, 상품 검색·변형 선택·수량 정확도·환각 여부를 자동 검증한다. 커머스 AI를 개발하는 한국 팀이라면, SFT만으로는 커버하기 어려운 멀티턴 트랜잭션 정확도를 RL로 끌어올리는 구체적 방법론으로 참고할 만하다.

[원문 보기 →](https://huggingface.co/blog/ecom-rlve) (Hugging Face Blog)

---

*본 포스트는 Claude Haiku 4.5로 자동 큐레이션·요약되었습니다. 
각 항목의 저작권은 원저작자에게 있으며, 본 사이트는 한국어 요약과 원문 링크만 제공합니다. 
오류·문의는 [이슈](https://github.com/prscsl/llm-mcp-weekly/issues)로 남겨주세요.*

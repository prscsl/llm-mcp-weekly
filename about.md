---
layout: single
title: 이 사이트에 대해
permalink: /about/
author_profile: false
sidebar:
  nav: "docs"
---

## LLM·MCP 위클리란

**LLM·MCP 위클리**는 Claude·MCP(Model Context Protocol)·LLM 생태계의 영문 소식을 매일 자동 수집하고, Claude로 한국어 요약·큐레이션하여 발행하는 기술 뉴스 블로그입니다.

타겟 독자는 한국의 백엔드/데이터 엔지니어 중 AI 도구를 실무에 통합하려는 분들입니다. 단순 번역이 아니라, **"현업 엔지니어 관점에서 이게 왜 중요한가"** 를 기준으로 내용을 선별합니다.

---

## 운영 방식

이 사이트는 자동화 파이프라인 기반의 개인 프로젝트로 운영됩니다. 모든 발행물은 코드와 정책에 의해 일관성을 유지하며, 발행 전 품질 점검을 거칩니다.

---

## 콘텐츠 수집 및 발행 방식

### 자동화 파이프라인

매일 아침 6시(KST) 자동 실행되며 다음 순서로 콘텐츠가 생성됩니다:

1. **수집** — 주요 영문 기술 뉴스 소스(공식 블로그 RSS, GitHub Releases, Hacker News)에서 LLM·MCP·Claude 관련 항목 필터링
2. **요약** — 수집된 원문을 Claude로 전달하여 한국어 요약 생성
3. **발행** — Jekyll 포스트로 자동 빌드 후 GitHub Pages에 배포

### AI 사용 고지

이 사이트의 요약 콘텐츠는 **Anthropic의 Claude가 생성**합니다. 원문 출처는 각 포스트에 명시됩니다.

---

## 콘텐츠 정책

- **출처 명시** — 모든 포스트에 원문 URL과 출처를 표기합니다.
- **저작권 준수** — 원문 전문을 복제하지 않으며, 요약 및 코멘트 형식으로 제공합니다. 원문 저작권자가 게재 중단을 요청하면 즉시 삭제합니다.
- **정확성** — AI 요약의 한계로 오류가 있을 수 있습니다. 중요한 내용은 반드시 원문을 직접 확인하세요.
- **광고** — Google AdSense를 통해 디스플레이 광고를 운영할 수 있으며, 광고 노출은 콘텐츠 선별 기준에 영향을 주지 않습니다.
- **개인정보** — 이 사이트는 별도의 회원가입이나 개인정보 수집을 하지 않습니다. 방문 통계는 Google Analytics로 집계될 수 있습니다.

---

## 데이터 소스

- Anthropic News
- Hugging Face Blog
- Simon Willison's Weblog
- LangChain Blog
- Pinecone Learn
- Latent Space
- Sebastian Raschka (Magazine)
- Lilian Weng's Log
- OpenAI Blog
- GitHub Releases — modelcontextprotocol/\*, anthropics/\*, block/goose, cline/cline, All-Hands-AI/OpenHands, continuedev/continue, langchain-ai/langgraph
- HackerNews (Algolia Search API)

---

## 문의

오류 제보, 다뤄주길 원하는 주제, 기타 문의는 GitHub Issues로 남겨주세요.

→ [GitHub Issues로 이동](https://github.com/prscsl/llm-mcp-weekly/issues)

---

*마지막 업데이트: 2026년 5월*

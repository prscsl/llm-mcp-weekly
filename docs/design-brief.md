# UI/UX 발전 및 수익화 기획 레퍼런스

**문서 목적**: Claude Design(또는 디자이너)에게 전달할 디자인 브리프.
와이어프레임·디자인 시스템·광고 슬롯 배치·페이지 구조 설계 의뢰용 참조 자료.

**작성**: 2026-04-27 / **사이트**: https://prscsl.github.io/llm-mcp-weekly/

---

## 1. 사이트 정체성 (변경 불가)

| 항목 | 내용 |
|------|------|
| 사이트명 | LLM·MCP 위클리 |
| 태그라인 | 한국 엔지니어를 위한 AI 생태계 정보지 |
| 설명 | Claude·MCP·LLM 생태계 영문 소식을 매일 한국어로 요약. 백엔드·데이터 엔지니어를 위한 실무 중심 기술 뉴스 |
| 운영자 | 박성수 (prscsl) — 데이터 파이프라인 엔지니어 |
| 운영 방식 | 자동 큐레이션: 수집 → Claude AI 한국어 요약 → 자동 발행 |
| 발행 주기 | 매일 06:00 KST |
| 스택 | Jekyll + Minimal Mistakes 테마 + GitHub Pages |
| URL | `prscsl.github.io/llm-mcp-weekly/` (자체 도메인 검토 중) |
| 리포 | github.com/prscsl/llm-mcp-weekly |

---

## 2. 콘텐츠 정책 (반드시 유지)

> 디자인이 이 정책을 시각적으로 보강해야 한다. 절대 약화시키면 안 됨.

- **저작권 존중**: 영문 원문 직접 인용·번역 금지 (자체 해석 + 한국 개발자 관점 의미만)
- **과장 금지**: 클릭베이트 / 낚시 제목 / "충격" 같은 어휘 금지
- **추측 금지**: 원문에 없는 사실 추가 금지
- **출처 명시**: 모든 항목에 원문 링크 + 출처 매체명 노출
- **AI 생성 disclosure**: 모든 포스트 하단에 "Claude AI로 자동 큐레이션·요약" 명시 — 시각적으로 약화되지 않게 디자인할 것
- **타겟 적합성**: 한국 백엔드·데이터·AI 엔지니어 실무에 가치 있는 항목만 발행

---

## 3. 현재 콘텐츠 구조

### 3-1. 데이터 소스 (확장 가능)
- RSS 9개 (Anthropic, HuggingFace, Simon Willison, LangChain, Pinecone, Latent Space, Sebastian Raschka, Lilian Weng, OpenAI)
- GitHub Releases 11개 (MCP SDK 3종, Anthropic 3종, 에이전트 도구 5종)
- HackerNews 키워드 7개 (claude, anthropic, mcp 등)

### 3-2. 일일 포스트 구조
```
제목: "{YYYY-MM-DD} LLM·MCP 위클리"
↓
도입부 (총 N건, 출처)
↓
카테고리별 그룹 (### 헤더):
  - 릴리스 소식
  - 도구 / 라이브러리
  - 업계 뉴스
  - 의견 / 분석
  - 연구 / 논문
  - 튜토리얼 / 가이드
↓
각 항목:
  ####  한국어 제목 (40자 이내)
  2~3문장 요약 + 한국 개발자 관점 의미 1문장
  > HN 점수 · 토론 링크 (HN 출처 시)
  [원문 보기 →](url) (출처 매체)
↓
푸터: AI 생성 disclosure + 이슈 링크
```

### 3-3. 페이지 구성
- 홈 (`/`): 포스트 목록 + 페이지네이션 (10개/페이지)
- 개별 포스트 (`/weekly/YYYY/MM/DD/llm-mcp-daily.html`)
- About (`/about/`): 운영자 + 파이프라인 + 정책

### 3-4. 현재 디자인 상태
- Minimal Mistakes default skin (다크모드 없음)
- 사이드바: 작가 프로필 (박성수, GitHub 링크만)
- 검색 / 카테고리 페이지 / 태그 페이지 없음
- 모바일 반응형 (테마 기본)
- 한글 폰트: 시스템 기본 (Pretendard 미적용)

---

## 4. UI/UX 발전 방향 (디자이너 의뢰 영역)

### 4-1. 정보 구조 (IA)

**문제**: 모든 포스트가 동일한 형식으로 보여 어떤 날 어떤 주제가 다뤄졌는지 한눈에 안 보임.

**개선**:
- 카테고리 허브 페이지 (`/category/release/`, `/category/news/`...)
- 태그 페이지 + 태그 클라우드
- 주제별 큐레이션 페이지 ("Claude Code 모음", "MCP 서버 모음")
- 검색 (jekyll-search 정적 인덱스, 추후 Algolia)
- 시간 아카이브 (월별)

### 4-2. 읽기 경험

**문제**: 항목 7~15개가 시각적으로 동일 비중이라 우선순위 안 보임.

**개선**:
- 항목별 카테고리 배지 (색상 코드)
- HN 고득점 항목 강조 (예: 300점+ 별 표시)
- 도입부에 "오늘의 핵심 1줄 요약"
- 코드 영역 / 인용 / 외부 링크 시각 구분 강화
- **한글 가독성 우선**: line-height ≥ 1.7, letter-spacing 미세 조정, Pretendard 폰트
- 다크 모드 (개발자 사용자층 선호)

### 4-3. 네비게이션 & 발견

**현재**: 상단 "홈 / About"뿐.

**개선**:
- 상단: 홈 / 카테고리 / 태그 / About / 구독
- 사이드바(데스크톱): 인기 태그 / 최근 발행 / 관련 포스트
- 푸터: 사이트맵 / RSS / 이메일 구독 / 소셜
- 포스트 내 인접 포스트 (이전/다음) 강화
- Related posts 알고리즘 (카테고리·태그 기반)

### 4-4. 참여 (Engagement)

- 이메일 구독: Buttondown 또는 Substack — 일일 발송 + 주간 다이제스트
- RSS (현재 jekyll-feed 적용됨, 강조 필요)
- 소셜 공유 버튼 (X, LinkedIn, Threads)
- Giscus 댓글 (GitHub Discussions 기반 — AdSense 정책과 충돌 없음)

### 4-5. 신뢰 시그널

- 사이드바 작가 프로필 강화 (사진·bio·이력)
- AI 생성 콘텐츠 시각적 disclosure (배지 + 푸터 둘 다)
- **개인정보 처리 방침 페이지** (AdSense 필수)
- **광고 정책 페이지** (sponsored 표기 방식)
- **정정 정책 페이지** (오류 신고·수정 절차)

---

## 5. 수익화 전략

### Phase 1 — Google AdSense (1~2개월)

**전제 조건**:
- 자체 도메인 권장 (서브경로 도메인은 승인률 낮음)
- 콘텐츠 30~50개 (현재 ~10개, 약 3주 후 충족)
- About / 개인정보 처리 방침 / 콘텐츠 정책 페이지 필수
- 트래픽 폭증 불필요 — 콘텐츠 품질·정책 페이지 위주

**광고 슬롯 후보** (디자이너에게 와이어프레임 의뢰):

| 위치 | 데스크톱 사이즈 | 모바일 사이즈 | 비고 |
|------|----------------|---------------|------|
| 1. 포스트 본문 인-콘텐츠 | 728×90 | 320×100 | 카테고리 사이 |
| 2. 사이드바 | 300×250 / 300×600 | 비표시 | 데스크톱만 |
| 3. 포스트 하단 (관련 포스트 위) | 728×90 | 320×100 | |
| 4. 홈 페이지네이션 사이 | 728×90 | 320×100 | 포스트 3개당 1개 |

**디자인 제약**:
- **CLS ≤ 0.1**: 광고 영역 reserved space 확보 (height 미리 잡기)
- 모바일 최우선: 화면 폭 ≥320px 대응
- Above-the-fold 광고 비율 50% 이하 (Google 정책)
- 광고-콘텐츠 시각 구분 (border + "광고 / Sponsored" 라벨)

**예상 수익** (한국 IT 콘텐츠 RPM 기준):
- 일 PV 500 → 월 $7~30
- 일 PV 1,000 → 월 $15~60
- 일 PV 5,000 → 월 $75~300 (Claude Max $100 회수 가능 구간)

### Phase 2 — 뉴스레터 + 후원 (3~6개월)

- Buttondown 또는 Substack
- 일일 발송 + 주간 다이제스트
- 구독자 1,000명 도달 시 한국 AI 회사 후원 영업
  - 타겟: 업스테이지, 솔트룩스, Liner, 네이버 클로바, 카카오 KAA, 라이너, 트웰브랩스 등
- 한국 IT 뉴스레터 후원 시세: 200,000~500,000원/회 (구독자 수 기반)

### Phase 3 — 어필리에이트 (병행 가능)

- 클라우드 크레딧 어필리에이트 (AWS, GCP)
- AI 도구 (Cursor, Claude Code Pro, Linear 등)
- 도서 (Yes24, 교보문고, 오라일리, Manning)
- **명시적 disclosure 의무**: "이 링크는 어필리에이트입니다"

### Phase 4 — Premium Tier (선택, 6개월 이후)

- 무료: 일일 영문 소식 한국어 요약 (현재)
- 유료 ($5/월 또는 5,500원/월):
  - 주간 deep-dive (한국 시장 적용 사례 분석)
  - 한국 AI 인프라 인터뷰 시리즈
  - Slack/Discord 커뮤니티 액세스
- 결제: Stripe(글로벌) + 토스페이먼츠/포트원(국내)

### 절대 안 하는 것 (정책)

- 클릭베이트 / 가짜 광고 / 네이티브 광고를 본 콘텐츠로 위장
- AI 생성 콘텐츠 사실 은폐
- 부정확한 출처 / 표절 / 원문 무단 번역
- 사용자 데이터 판매
- AI 워싱 (실제로 AI를 쓰지 않은 걸 AI라 표기) — 반대도 마찬가지

---

## 6. 디자인 브리프 — 의뢰할 산출물 목록

### 6-1. 핵심 산출물

1. **디자인 시스템 (DESIGN.md 또는 Figma)**
   - 색상 팔레트 (라이트 + 다크)
   - 타이포그래피 (Pretendard 1순위, Noto Sans KR 폴백)
   - 간격 시스템 (8 / 16 / 24 / 32 / 48 / 64)
   - 컴포넌트: 카드, 카테고리 배지, 버튼, 폼, 광고 슬롯 frame

2. **페이지 와이어프레임 (모바일 우선, 데스크톱 병행)**
   - 홈 (포스트 리스트 + 광고 슬롯 4번)
   - 개별 포스트 (본문 + 광고 슬롯 1·3 + 관련 포스트)
   - 카테고리 / 태그 페이지
   - About / 개인정보 / 광고 정책 / 정정 정책
   - 검색 결과 페이지

3. **광고 슬롯 가이드**
   - AdSense 4개 위치 별 사이즈, reserved space, 시각 처리
   - CLS 0.1 이하 보장 방법 (예: aspect-ratio 사전 지정)

4. **이메일 구독 폼**
   - 헤더 / 푸터 / 사이드바 / 인라인 4개 위치 변형

5. **AI 생성 콘텐츠 disclosure 컴포넌트**
   - 포스트 상단 (작은 배지) + 하단 (전체 disclosure 박스)

6. **로고 / OG 이미지 리뉴얼** (현재 placeholder)

### 6-2. 제약 조건 (변경 불가)

- **베이스**: Jekyll + Minimal Mistakes 테마 (전면 교체 X, SCSS 오버라이드로 커스텀)
- **baseurl**: `/llm-mcp-weekly` (서브경로) — 자체 도메인 이전 시 변경 가능
- **자동 발행 파이프라인 호환**: `_layouts/post.html`, `_includes/`만 커스텀. 마크다운 frontmatter 형식 변경 시 [scripts/publish.py](../scripts/publish.py) 동시 수정 필수
- **GitHub Actions 빌드 시간 5분 이내 유지**: 폰트 self-host 시 용량 주의, 이미지 최적화
- **한국어 콘텐츠 우선**: 한글 가독성 / 폰트 / 줄높이를 영문보다 우선 고려

### 6-3. 참고 사이트 (벤치마킹)

| 사이트 | 참고 포인트 |
|------|------|
| **TLDR.tech** | 일일 IT 뉴스레터, 시각적 정보 밀도, 광고 통합 |
| **The Pragmatic Engineer** | 신뢰감 있는 엔지니어 콘텐츠 톤 |
| **Stratechery** | 유료 뉴스레터 페이월·전환 UX |
| **Hacker News** | 정보 밀도 (참고용, 그대로 카피 X) |
| **김재성 블로그 (jojoldu.tistory.com)** | 한국 백엔드 엔지니어 블로그 톤 |
| **Outsider's Dev Story** | 한국 개발자 블로그 |
| **블루프린트 / Slowletter** | 한국 IT 뉴스레터 |
| **GeekNews** | 한국 개발자 친숙 톤·정보 밀도 |

### 6-4. KPI (디자인이 영향을 주는 지표)

- 평균 체류시간 (현재 미측정 → GA4 도입 필요)
- 페이지뷰 / 세션
- 모바일 vs 데스크톱 비율
- 이메일 구독 전환율
- AdSense RPM, viewability
- Core Web Vitals: LCP / CLS / INP
- Search Console CTR

---

## 7. 단계별 로드맵

### Phase 1 (1~2주): 기초 정비
- [ ] Google Search Console 등록 + sitemap 제출
- [ ] Naver Search Advisor 등록
- [ ] GA4 도입 (현재 _config.yml에 placeholder만 있음)
- [ ] 개인정보 처리 방침 / 정정 정책 / 광고 정책 페이지 추가
- [ ] AI 생성 콘텐츠 disclosure 시각적 강화

### Phase 2 (2~4주): UI/UX 개선 (디자이너 산출물 적용)
- [ ] 디자인 시스템 적용 (Pretendard, 다크모드, 색상)
- [ ] 카테고리 / 태그 페이지 추가
- [ ] 검색 도입 (jekyll-search)
- [ ] 광고 슬롯 reserved space 디자인
- [ ] AdSense 신청

### Phase 3 (1~2개월): 수익화 본격화
- [ ] AdSense 승인 후 광고 게재
- [ ] Buttondown 뉴스레터 런치
- [ ] Giscus 댓글
- [ ] 자체 도메인 이전 검토 (`llm-mcp-weekly.com` 또는 `.kr`)

### Phase 4 (3~6개월): 확장
- [ ] 한국 AI 회사 후원 영업
- [ ] 어필리에이트 통합
- [ ] Premium tier 검토 (구독자 1,000명 도달 시)

---

## 8. Claude Design 전달 시 첨부할 정보

- 라이브 사이트 (현재 톤·정보 밀도 파악용)
  - 홈: https://prscsl.github.io/llm-mcp-weekly/
  - 포스트 예: https://prscsl.github.io/llm-mcp-weekly/weekly/2026/04/26/llm-mcp-daily.html
  - About: https://prscsl.github.io/llm-mcp-weekly/about/
- 현재 _config.yml: minimal_mistakes_skin = `default`
- 현재 logo: `assets/images/logo.png` (placeholder, 교체 가능)
- 현재 OG: `assets/images/og-default.png` (placeholder, 교체 가능)
- 운영자 프로필: 박성수, 데이터 파이프라인 엔지니어, GitHub 링크만
- 한국 사용자 폰트 우선순위: Pretendard > Noto Sans KR > 시스템 기본

---

## 9. 디자이너에게 묻고 싶은 것 (의사결정 포인트)

1. 다크 모드 우선 vs 라이트 우선?
2. 광고 슬롯 4개 모두 활용 vs 사용자 경험 우선해 2~3개로 축소?
3. 카테고리 색상 코드 — 의미 기반(릴리스=녹색, 뉴스=파랑, 의견=회색...) vs 단조 톤?
4. 모바일에서 사이드바를 드로어로 vs 하단 시트로?
5. 검색 — 항상 노출 vs 아이콘 클릭 시 expand?
6. 이메일 구독 폼 위치 — 푸터만 vs 포스트 하단 + 푸터?
7. AI disclosure 강도 — 작은 배지 vs 큰 박스 vs 둘 다?

---

**문서 끝**. 의뢰 후 디자이너 피드백·결정 사항은 본 문서에 누적 업데이트.

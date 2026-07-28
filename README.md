# 프레자일 AI Brand Intelligence System — 자동 수집기 (Tier B)

Google Trends + Reddit 데이터를 매일 자동으로 수집해 `data/` 폴더에 CSV로 누적 저장합니다.
Google Ads / TikTok / Amazon은 아직 여기 포함되어 있지 않습니다 (별도 설명 참고).

## 1. 로컬에서 먼저 테스트하기

```bash
pip install -r requirements.txt

# Reddit API 키 발급: https://www.reddit.com/prefs/apps → "create app" → type: script
export REDDIT_CLIENT_ID="발급받은_id"
export REDDIT_CLIENT_SECRET="발급받은_secret"
export REDDIT_USER_AGENT="presail-brand-intel/1.0"

python run_daily.py
```

정상 작동하면 `data/google_trends_history.csv`, `data/reddit_history.csv` 두 파일이 생깁니다.

## 2. 매일 자동 실행하기 (GitHub Actions, 무료)

1. 이 폴더 전체를 새 GitHub 저장소(private 추천)에 업로드
2. 저장소 Settings → Secrets and variables → Actions → New repository secret 에서
   - `REDDIT_CLIENT_ID`
   - `REDDIT_CLIENT_SECRET`
   두 개 등록
3. `.github/workflows/daily_collect.yml` 이 이미 포함되어 있어서, 저장소에 올리는 순간부터
   **매일 한국시간 오전 7시에 자동 실행**되고, 결과가 `data/` 폴더에 자동 커밋됩니다.
4. Actions 탭에서 "Run workflow" 버튼으로 지금 바로 수동 실행도 가능합니다.

## 3. 데이터를 저에게 넘기는 법

매주 한 번 정도, `data/google_trends_history.csv`와 `data/reddit_history.csv`를 저한테 올려주시면
지난주 대비 급상승 키워드를 뽑아 리포트로 정리해드릴 수 있어요.
(이 부분도 나중에는 예약 리포트에 자동 첨부되도록 연결 가능합니다.)

## 4. 아직 자동화되지 않은 부분과 이유

| 소스 | 이유 | 임시 대안 |
|---|---|---|
| Google Ads 검색량 | 공식 API는 개발자 토큰 승인 필요 (며칠~몇 주) | 승인 신청 먼저 진행 → 승인되면 코드 추가해드림 |
| TikTok Creative Center | 공개 API 없음, 스크래핑은 이용약관 위반 소지 | 주 1회 수동 CSV 내보내기 유지 |
| Amazon Best Seller | 공식 API는 제휴사 대상이라 제약 있음 | Claude 예약 리포트에서 웹 검색으로 보완 |

## 5. 키워드/서브레딧 수정

`config.py` 파일 하나만 수정하면 전체 시스템에 반영됩니다. 코드를 건드릴 필요 없습니다.

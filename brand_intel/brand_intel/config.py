"""
프레자일 AI Brand Intelligence System - 설정 파일
여기서 키워드/서브레딧 리스트만 수정하면 전체 시스템에 반영됩니다.
"""

# ── 추적할 키워드 (뷰티/스킨케어) ──────────────────────────────
# 필요할 때마다 자유롭게 추가/삭제하세요.
KEYWORDS = [
    "skin barrier",
    "milky toner",
    "glass skin",
    "pdrn",
    "collagen",
    "korean sunscreen",
    "sleeping mask",
    "oil cleanser",
    "double cleansing",
    "hypochlorous acid",
    "snail mucin",
    "centella",
    "niacinamide",
    "ceramide",
]

# ── Reddit에서 모니터링할 서브레딧 ────────────────────────────
SUBREDDITS = [
    "SkincareAddiction",
    "AsianBeauty",
    "KoreanBeauty",
    "30PlusSkinCare",
    "SkincareAddicts",
]

# 검색 기간 (최근 N일 이내 게시물만 카운트)
REDDIT_LOOKBACK_DAYS = 7

# Reddit 검색당 최대 게시물 수 (API 부하 방지)
REDDIT_LIMIT_PER_KEYWORD = 50

# ── Google Trends 설정 ────────────────────────────────────────
TRENDS_GEO = "US"          # 미국 시장 기준
TRENDS_TIMEFRAME = "now 7-d"  # 최근 7일 관심도 추이

# ── 데이터 저장 경로 ───────────────────────────────────────────
DATA_DIR = "data"

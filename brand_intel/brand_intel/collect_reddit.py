"""
Reddit 수집기
- 공식 Reddit API(PRAW)를 사용합니다. 무료이며 앱 등록만 하면 바로 사용 가능합니다.
- 지정된 서브레딧들에서 키워드별 최근 언급량(게시물 수, 평균 추천수)을 매일 집계해
  CSV에 누적 저장합니다.

사전 준비:
1. https://www.reddit.com/prefs/apps 에서 "script" 타입 앱 생성 (무료, 즉시 발급)
2. client_id, client_secret 발급받기
3. 아래 3개를 환경변수로 등록:
   REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

설치: pip install praw pandas
"""

import os
import datetime
import pandas as pd
import praw

from config import (
    KEYWORDS, SUBREDDITS, REDDIT_LOOKBACK_DAYS,
    REDDIT_LIMIT_PER_KEYWORD, DATA_DIR,
)

OUTPUT_FILE = os.path.join(DATA_DIR, "reddit_history.csv")


def get_reddit_client():
    return praw.Reddit(
        client_id=os.environ["REDDIT_CLIENT_ID"],
        client_secret=os.environ["REDDIT_CLIENT_SECRET"],
        user_agent=os.environ.get("REDDIT_USER_AGENT", "presail-brand-intel/1.0"),
    )


def main():
    os.makedirs(DATA_DIR, exist_ok=True)
    reddit = get_reddit_client()

    cutoff = datetime.datetime.utcnow() - datetime.timedelta(days=REDDIT_LOOKBACK_DAYS)
    today = datetime.date.today().isoformat()
    rows = []

    subreddit_str = "+".join(SUBREDDITS)  # 여러 서브레딧 동시 검색
    combined_sub = reddit.subreddit(subreddit_str)

    for kw in KEYWORDS:
        try:
            posts = list(combined_sub.search(kw, sort="new", time_filter="week",
                                               limit=REDDIT_LIMIT_PER_KEYWORD))
        except Exception as e:
            print(f"[경고] '{kw}' 검색 실패: {e}")
            continue

        recent_posts = [
            p for p in posts
            if datetime.datetime.utcfromtimestamp(p.created_utc) >= cutoff
        ]

        if not recent_posts:
            mention_count, avg_score, avg_comments = 0, 0, 0
        else:
            mention_count = len(recent_posts)
            avg_score = sum(p.score for p in recent_posts) / mention_count
            avg_comments = sum(p.num_comments for p in recent_posts) / mention_count

        rows.append({
            "date": today,
            "keyword": kw,
            "mention_count_7d": mention_count,
            "avg_upvotes": round(avg_score, 1),
            "avg_comments": round(avg_comments, 1),
        })

    new_df = pd.DataFrame(rows)

    if os.path.exists(OUTPUT_FILE):
        old_df = pd.read_csv(OUTPUT_FILE)
        combined = pd.concat([old_df, new_df], ignore_index=True)
        combined.drop_duplicates(subset=["date", "keyword"], keep="last", inplace=True)
    else:
        combined = new_df

    combined.to_csv(OUTPUT_FILE, index=False)
    print(f"저장 완료: {OUTPUT_FILE} ({len(new_df)}개 신규 행)")


if __name__ == "__main__":
    main()

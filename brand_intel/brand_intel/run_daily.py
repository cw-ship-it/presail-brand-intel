"""
매일 실행되는 메인 스크립트.
GitHub Actions나 cron이 이 파일 하나만 실행하면 됩니다.
"""

import subprocess
import sys


def run(script_name):
    print(f"\n=== {script_name} 실행 ===")
    result = subprocess.run([sys.executable, script_name])
    if result.returncode != 0:
        print(f"[경고] {script_name} 실행 중 오류 발생 (계속 진행)")


if __name__ == "__main__":
    run("collect_google_trends.py")
    run("collect_reddit.py")
    print("\n모든 수집 완료. data/ 폴더에 CSV로 누적 저장됨.")

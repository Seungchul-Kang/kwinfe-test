"""
GitHub Issues 자동 생성 스크립트
사용법:
1. GitHub Personal Access Token을 생성하세요 (https://github.com/settings/tokens)
2. 'repo' 권한을 체크하세요
3. 이 스크립트를 실행하고 토큰을 입력하세요: python create_issues.py
"""

import os
import json
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("requests 모듈이 설치되어 있지 않습니다.")
    print("다음 명령으로 설치하세요: pip install requests")
    sys.exit(1)

# 저장소 정보
OWNER = "Seungchul-Kang"
REPO = "kwinfe-test"
API_URL = f"https://api.github.com/repos/{OWNER}/{REPO}/issues"

# 이슈 파일 정보
ISSUES = [
    {
        "file": "phase1-project-setup.md",
        "title": "Phase 1: 프로젝트 초기 설정",
        "labels": ["setup", "phase-1", "priority-high"]
    },
    {
        "file": "phase2-django-apps.md",
        "title": "Phase 2: Django 앱 생성 및 설정",
        "labels": ["feature", "phase-2", "priority-high"]
    },
    {
        "file": "phase3-database-setup.md",
        "title": "Phase 3: 데이터베이스 설정",
        "labels": ["database", "phase-3", "priority-high"]
    },
    {
        "file": "phase4-url-routing.md",
        "title": "Phase 4: URL 라우팅 설정",
        "labels": ["configuration", "phase-4", "priority-medium"]
    },
    {
        "file": "phase5-template-development.md",
        "title": "Phase 5: 템플릿 개발",
        "labels": ["frontend", "templates", "phase-5", "priority-high"]
    },
    {
        "file": "phase6-views-logic.md",
        "title": "Phase 6: Views 및 로직 구현",
        "labels": ["backend", "views", "phase-6", "priority-high"]
    },
    {
        "file": "phase7-static-files.md",
        "title": "Phase 7: 정적 파일 및 스타일링",
        "labels": ["frontend", "css", "javascript", "phase-7", "priority-medium"]
    },
    {
        "file": "phase8-security.md",
        "title": "Phase 8: 보안 및 인증 강화",
        "labels": ["security", "phase-8", "priority-high"]
    },
    {
        "file": "phase9-testing.md",
        "title": "Phase 9: 테스트 작성",
        "labels": ["testing", "phase-9", "priority-high"]
    },
    {
        "file": "phase10-documentation.md",
        "title": "Phase 10: 문서화 및 배포 준비",
        "labels": ["documentation", "phase-10", "priority-medium"]
    }
]


def create_issue(token, title, body, labels):
    """GitHub 이슈 생성"""
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    data = {
        "title": title,
        "body": body,
        "labels": labels
    }
    
    # SSL 인증서 검증 오류를 우회하기 위해 verify=False 추가
    # 주의: 프로덕션 환경에서는 권장하지 않음
    try:
        response = requests.post(API_URL, headers=headers, json=data, verify=False)
    except requests.exceptions.SSLError:
        # SSL 오류 시 재시도
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        response = requests.post(API_URL, headers=headers, json=data, verify=False)
    
    return response


def main():
    # 토큰 입력
    print("=" * 60)
    print("GitHub Issues 자동 생성 스크립트")
    print("=" * 60)
    print()
    
    # 환경 변수에서 토큰 읽기
    token = os.environ.get("GITHUB_TOKEN")
    
    if not token:
        print("GitHub Personal Access Token이 필요합니다.")
        print("1. https://github.com/settings/tokens 접속")
        print("2. 'Generate new token (classic)' 클릭")
        print("3. 'repo' 권한 체크")
        print("4. 생성된 토큰 복사")
        print()
        token = input("GitHub Token을 입력하세요: ").strip()
        
        if not token:
            print("❌ 토큰이 입력되지 않았습니다.")
            sys.exit(1)
    else:
        print("✓ 환경 변수에서 GITHUB_TOKEN을 찾았습니다.")
    
    print()
    print(f"저장소: {OWNER}/{REPO}")
    print(f"이슈 개수: {len(ISSUES)}개")
    print()
    print("이슈 생성을 시작합니다...")
    print("-" * 60)
    
    issues_dir = Path("docs/issues")
    created_count = 0
    failed_count = 0
    
    for issue_info in ISSUES:
        file_path = issues_dir / issue_info["file"]
        
        if not file_path.exists():
            print(f"❌ 파일을 찾을 수 없음: {file_path}")
            failed_count += 1
            continue
        
        # 파일 내용 읽기
        with open(file_path, "r", encoding="utf-8") as f:
            body = f.read()
        
        # 이슈 생성
        response = create_issue(
            token=token,
            title=issue_info["title"],
            body=body,
            labels=issue_info["labels"]
        )
        
        if response.status_code == 201:
            issue_data = response.json()
            print(f"✅ {issue_info['title']}")
            print(f"   URL: {issue_data['html_url']}")
            created_count += 1
        else:
            print(f"❌ {issue_info['title']}")
            print(f"   오류: {response.status_code} - {response.text}")
            failed_count += 1
    
    print("-" * 60)
    print()
    print("완료!")
    print(f"✅ 생성 성공: {created_count}개")
    if failed_count > 0:
        print(f"❌ 생성 실패: {failed_count}개")
    print()
    print("GitHub Issues 페이지:")
    print(f"https://github.com/{OWNER}/{REPO}/issues")


if __name__ == "__main__":
    main()

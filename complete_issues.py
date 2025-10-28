"""
GitHub Issues 자동 완료 처리 스크립트

이 스크립트는:
1. 각 Phase별 이슈를 생성
2. 완료 코멘트를 작성
3. 이슈를 닫습니다

사용법:
1. GitHub Personal Access Token 생성 (repo 권한 필요)
2. PowerShell에서 실행:
   $env:GITHUB_TOKEN = "your_token_here"
   python complete_issues.py
"""

import os
import requests
import json
import time

# GitHub 설정
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_OWNER = 'Seungchul-Kang'
REPO_NAME = 'kwinfe-test'
API_BASE = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}'

# Headers
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
    'Content-Type': 'application/json'
}

# Phase 정보
phases = [
    {
        'number': 1,
        'title': 'Phase 1: 프로젝트 초기 설정',
        'file': 'docs/issues/phase1-project-setup.md',
        'commit': '4939340',
        'labels': ['setup', 'phase-1', 'priority-high']
    },
    {
        'number': 2,
        'title': 'Phase 2: Django 앱 생성 및 설정',
        'file': 'docs/issues/phase2-django-apps.md',
        'commit': '6aa9895',
        'labels': ['feature', 'phase-2', 'priority-high']
    },
    {
        'number': 3,
        'title': 'Phase 3: 데이터베이스 설정',
        'file': 'docs/issues/phase3-database-setup.md',
        'commit': '67464ad',
        'labels': ['database', 'phase-3', 'priority-high']
    },
    {
        'number': 4,
        'title': 'Phase 4: URL 라우팅 설정',
        'file': 'docs/issues/phase4-url-routing.md',
        'commit': 'd699afa',
        'labels': ['feature', 'phase-4', 'priority-medium']
    },
    {
        'number': 5,
        'title': 'Phase 5: 템플릿 개발',
        'file': 'docs/issues/phase5-template-development.md',
        'commit': 'd6c6ed5',
        'labels': ['frontend', 'phase-5', 'priority-high']
    },
    {
        'number': 6,
        'title': 'Phase 6: Views 및 로직 구현',
        'file': 'docs/issues/phase6-views-logic.md',
        'commit': '6aa9895',  # Phase 2와 함께 완료
        'labels': ['feature', 'phase-6', 'priority-high']
    },
    {
        'number': 7,
        'title': 'Phase 7: 정적 파일 및 스타일링',
        'file': 'docs/issues/phase7-static-files.md',
        'commit': 'd6c6ed5',  # Phase 5와 함께 완료
        'labels': ['frontend', 'phase-7', 'priority-medium']
    },
    {
        'number': 8,
        'title': 'Phase 8: 보안 및 인증 강화',
        'file': 'docs/issues/phase8-security.md',
        'commit': 'e161f89',
        'labels': ['security', 'phase-8', 'priority-high']
    },
    {
        'number': 9,
        'title': 'Phase 9: 테스트 작성',
        'file': 'docs/issues/phase9-testing.md',
        'commit': 'e161f89',
        'labels': ['testing', 'phase-9', 'priority-medium']
    },
    {
        'number': 10,
        'title': 'Phase 10: 문서화 및 배포 준비',
        'file': 'docs/issues/phase10-documentation.md',
        'commit': 'e161f89',
        'labels': ['documentation', 'phase-10', 'priority-medium']
    }
]

# 완료 코멘트 템플릿
completion_template = """## ✅ Phase {number} 완료

이 Phase가 성공적으로 완료되었습니다!

### 📌 커밋 정보
- **커밋 해시**: `{commit}`
- **커밋 메시지**: {commit_message}
- **GitHub 커밋**: https://github.com/{owner}/{repo}/commit/{commit}

### 📝 주요 완료 내용
{completion_details}

### 🔗 관련 링크
- [전체 완료 보고서](https://github.com/{owner}/{repo}/blob/main/docs/PHASE_COMPLETION_REPORT.md)
- [프로젝트 README](https://github.com/{owner}/{repo}/blob/main/README.md)

---

**Status**: Completed ✅  
**Closed by**: Automated completion script  
**Date**: {date}
"""

def check_token():
    """GitHub Token 유효성 검사"""
    if not GITHUB_TOKEN:
        print("❌ 오류: GITHUB_TOKEN 환경 변수가 설정되지 않았습니다.")
        print("\nPowerShell에서 다음 명령을 실행하세요:")
        print('$env:GITHUB_TOKEN = "your_token_here"')
        return False
    
    # Token 테스트
    response = requests.get('https://api.github.com/user', headers=headers, verify=False)
    if response.status_code != 200:
        print(f"❌ 오류: GitHub Token이 유효하지 않습니다. (Status: {response.status_code})")
        return False
    
    user = response.json()
    print(f"✅ GitHub 인증 성공: {user['login']}")
    return True

def get_issue_body(file_path):
    """이슈 파일 내용 읽기"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # 첫 번째 # 제목 제거 (GitHub 이슈 타이틀로 사용됨)
            lines = content.split('\n')
            if lines[0].startswith('# '):
                return '\n'.join(lines[1:]).strip()
            return content
    except FileNotFoundError:
        print(f"⚠️  경고: {file_path} 파일을 찾을 수 없습니다.")
        return None

def create_issue(phase):
    """이슈 생성"""
    print(f"\n{'='*60}")
    print(f"📝 Phase {phase['number']} 이슈 생성 중...")
    
    body = get_issue_body(phase['file'])
    if not body:
        print(f"⚠️  Phase {phase['number']} 이슈 본문을 로드할 수 없습니다. 건너뜁니다.")
        return None
    
    data = {
        'title': phase['title'],
        'body': body,
        'labels': phase['labels']
    }
    
    response = requests.post(f"{API_BASE}/issues", headers=headers, json=data, verify=False)
    
    if response.status_code == 201:
        issue = response.json()
        print(f"✅ 이슈 생성 성공: #{issue['number']} - {phase['title']}")
        return issue['number']
    else:
        print(f"❌ 이슈 생성 실패: {response.status_code}")
        print(f"   응답: {response.text}")
        return None

def add_completion_comment(issue_number, phase):
    """완료 코멘트 추가"""
    print(f"💬 Phase {phase['number']} 완료 코멘트 작성 중...")
    
    # 커밋 정보 가져오기
    commit_response = requests.get(
        f"{API_BASE}/commits/{phase['commit']}", 
        headers=headers,
        verify=False
    )
    
    commit_message = "커밋 정보 로드 실패"
    if commit_response.status_code == 200:
        commit_data = commit_response.json()
        commit_message = commit_data['commit']['message']
    
    # 완료 내용 (간단한 버전)
    completion_details = f"Phase {phase['number']}의 모든 작업이 완료되었습니다. 자세한 내용은 [완료 보고서](https://github.com/{REPO_OWNER}/{REPO_NAME}/blob/main/docs/PHASE_COMPLETION_REPORT.md)를 참조하세요."
    
    comment_body = completion_template.format(
        number=phase['number'],
        commit=phase['commit'],
        commit_message=commit_message,
        owner=REPO_OWNER,
        repo=REPO_NAME,
        completion_details=completion_details,
        date=time.strftime('%Y-%m-%d %H:%M:%S')
    )
    
    data = {'body': comment_body}
    
    response = requests.post(
        f"{API_BASE}/issues/{issue_number}/comments",
        headers=headers,
        json=data,
        verify=False
    )
    
    if response.status_code == 201:
        print(f"✅ 완료 코멘트 작성 성공")
        return True
    else:
        print(f"❌ 코멘트 작성 실패: {response.status_code}")
        return False

def close_issue(issue_number, phase):
    """이슈 닫기"""
    print(f"🔒 Phase {phase['number']} 이슈 닫는 중...")
    
    data = {'state': 'closed'}
    
    response = requests.patch(
        f"{API_BASE}/issues/{issue_number}",
        headers=headers,
        json=data,
        verify=False
    )
    
    if response.status_code == 200:
        print(f"✅ 이슈 #{issue_number} 닫기 성공")
        return True
    else:
        print(f"❌ 이슈 닫기 실패: {response.status_code}")
        return False

def main():
    """메인 실행 함수"""
    print("="*60)
    print("🚀 GitHub Issues 자동 완료 처리 시작")
    print("="*60)
    
    # Token 검증
    if not check_token():
        return
    
    print(f"\n📊 처리할 Phase: {len(phases)}개")
    
    # 사용자 확인
    response = input("\n계속하시겠습니까? (y/n): ")
    if response.lower() != 'y':
        print("❌ 취소되었습니다.")
        return
    
    success_count = 0
    failed_count = 0
    
    for phase in phases:
        try:
            # 1. 이슈 생성
            issue_number = create_issue(phase)
            if not issue_number:
                failed_count += 1
                continue
            
            time.sleep(1)  # API Rate Limit 방지
            
            # 2. 완료 코멘트 추가
            if not add_completion_comment(issue_number, phase):
                failed_count += 1
                continue
            
            time.sleep(1)
            
            # 3. 이슈 닫기
            if not close_issue(issue_number, phase):
                failed_count += 1
                continue
            
            success_count += 1
            print(f"✅ Phase {phase['number']} 완료 처리 성공!")
            
            time.sleep(2)  # API Rate Limit 방지
            
        except Exception as e:
            print(f"❌ Phase {phase['number']} 처리 중 오류 발생: {e}")
            failed_count += 1
    
    # 최종 결과
    print("\n" + "="*60)
    print("📊 완료 결과")
    print("="*60)
    print(f"✅ 성공: {success_count}개")
    print(f"❌ 실패: {failed_count}개")
    print(f"📝 총 처리: {success_count + failed_count}개")
    
    if success_count > 0:
        print(f"\n🎉 {success_count}개의 이슈가 성공적으로 완료 처리되었습니다!")
        print(f"🔗 확인: https://github.com/{REPO_OWNER}/{REPO_NAME}/issues?q=is%3Aissue+is%3Aclosed")

if __name__ == '__main__':
    main()

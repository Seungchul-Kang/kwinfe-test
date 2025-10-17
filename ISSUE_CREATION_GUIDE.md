# GitHub Issues 자동 생성 가이드

## 🚀 빠른 시작

### 1단계: GitHub Personal Access Token 생성

1. https://github.com/settings/tokens 접속
2. **"Generate new token (classic)"** 클릭
3. Token 이름 입력 (예: "kwinfe-test-issues")
4. **`repo`** 권한 체크 ✅ (전체 repo 권한 필요)
5. **"Generate token"** 클릭
6. **생성된 토큰을 복사** (다시 볼 수 없으니 안전한 곳에 보관)

### 2단계: Python 스크립트 실행

#### 방법 A: 환경 변수 설정 후 실행 (권장)

```powershell
# PowerShell에서 실행
$env:GITHUB_TOKEN = "your_personal_access_token_here"
python create_issues.py
```

#### 방법 B: 직접 입력

```powershell
# PowerShell에서 실행
python create_issues.py
# 프롬프트가 나타나면 토큰 입력
```

### 3단계: 결과 확인

스크립트가 성공적으로 실행되면 다음과 같은 출력이 나타납니다:

```
============================================================
GitHub Issues 자동 생성 스크립트
============================================================

✓ 환경 변수에서 GITHUB_TOKEN을 찾았습니다.

저장소: Seungchul-Kang/kwinfe-test
이슈 개수: 10개

이슈 생성을 시작합니다...
------------------------------------------------------------
✅ Phase 1: 프로젝트 초기 설정
   URL: https://github.com/Seungchul-Kang/kwinfe-test/issues/1
✅ Phase 2: Django 앱 생성 및 설정
   URL: https://github.com/Seungchul-Kang/kwinfe-test/issues/2
...
------------------------------------------------------------

완료!
✅ 생성 성공: 10개

GitHub Issues 페이지:
https://github.com/Seungchul-Kang/kwinfe-test/issues
```

---

## 📋 생성될 이슈 목록

| # | 제목 | Labels | 우선순위 |
|---|------|--------|---------|
| 1 | Phase 1: 프로젝트 초기 설정 | setup, phase-1 | High |
| 2 | Phase 2: Django 앱 생성 및 설정 | feature, phase-2 | High |
| 3 | Phase 3: 데이터베이스 설정 | database, phase-3 | High |
| 4 | Phase 4: URL 라우팅 설정 | configuration, phase-4 | Medium |
| 5 | Phase 5: 템플릿 개발 | frontend, templates, phase-5 | High |
| 6 | Phase 6: Views 및 로직 구현 | backend, views, phase-6 | High |
| 7 | Phase 7: 정적 파일 및 스타일링 | frontend, css, javascript, phase-7 | Medium |
| 8 | Phase 8: 보안 및 인증 강화 | security, phase-8 | High |
| 9 | Phase 9: 테스트 작성 | testing, phase-9 | High |
| 10 | Phase 10: 문서화 및 배포 준비 | documentation, phase-10 | Medium |

---

## 🔧 문제 해결

### Python이 설치되지 않은 경우

```powershell
# Python 버전 확인
python --version

# Python이 없다면 https://www.python.org/downloads/ 에서 설치
```

### requests 모듈이 없는 경우

```powershell
pip install requests
```

### 토큰 권한 오류 (403)

- 토큰이 `repo` 권한을 가지고 있는지 확인
- 토큰이 만료되지 않았는지 확인
- 리포지토리에 쓰기 권한이 있는지 확인

### 이미 이슈가 존재하는 경우

스크립트를 다시 실행하면 중복된 이슈가 생성됩니다. 기존 이슈를 먼저 삭제하거나, 수동으로 관리하세요.

---

## 💡 추가 팁

### 토큰을 환경 변수로 영구 설정 (Windows)

```powershell
# 현재 사용자에 대해 영구적으로 설정
[System.Environment]::SetEnvironmentVariable('GITHUB_TOKEN', 'your_token', 'User')

# 새 터미널을 열어 확인
echo $env:GITHUB_TOKEN
```

### PowerShell 대신 사용할 수 있는 방법

#### Git Bash

```bash
export GITHUB_TOKEN="your_token"
python create_issues.py
```

#### CMD

```cmd
set GITHUB_TOKEN=your_token
python create_issues.py
```

---

## 🔒 보안 주의사항

- **토큰을 Git에 커밋하지 마세요!**
- `.env` 파일이나 환경 변수로만 관리하세요
- 토큰이 노출되면 즉시 https://github.com/settings/tokens 에서 삭제하세요
- 토큰은 필요한 최소 권한만 부여하세요

---

## 📞 도움이 필요하신가요?

문제가 발생하면:
1. 에러 메시지를 확인하세요
2. 위의 "문제 해결" 섹션을 참고하세요
3. GitHub Issues에 질문을 남겨주세요

---

**이제 스크립트를 실행하여 10개의 이슈를 자동으로 생성하세요!** 🎉

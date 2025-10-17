# ⚠️ 자동 이슈 생성 실패 - 수동 생성 가이드

자동 스크립트 실행 시 인증 오류(401)가 발생했습니다. 이는 다음과 같은 이유 때문일 수 있습니다:

1. **GitHub Token이 유효하지 않음**
2. **Token 권한이 부족함** (`repo` 권한 필요)
3. **Token이 만료됨**

## 🔧 해결 방법

### 옵션 1: 새 토큰으로 다시 시도

1. 새 Personal Access Token 생성:
   - https://github.com/settings/tokens
   - "Generate new token (classic)"
   - **`repo` 전체 권한 체크** ✅
   - 토큰 생성 후 복사

2. PowerShell에서 실행:
```powershell
# 새 토큰 설정
$env:GITHUB_TOKEN = "ghp_새로생성한토큰"

# 스크립트 재실행
python create_issues.py
```

---

### 옵션 2: GitHub 웹 인터페이스에서 수동 생성 (권장)

각 Phase별로 이슈를 수동으로 생성하는 것이 더 안전하고 확실합니다.

#### 단계별 가이드

**1. GitHub Issues 페이지로 이동**
   - https://github.com/Seungchul-Kang/kwinfe-test/issues

**2. "New issue" 버튼 클릭**

**3. 각 Phase 파일 열기 및 복사**

아래 경로에서 각 파일을 열어 내용을 복사합니다:

| Phase | 파일 경로 | 복사할 내용 |
|-------|----------|-----------|
| 1 | `docs/issues/phase1-project-setup.md` | 전체 내용 |
| 2 | `docs/issues/phase2-django-apps.md` | 전체 내용 |
| 3 | `docs/issues/phase3-database-setup.md` | 전체 내용 |
| 4 | `docs/issues/phase4-url-routing.md` | 전체 내용 |
| 5 | `docs/issues/phase5-template-development.md` | 전체 내용 |
| 6 | `docs/issues/phase6-views-logic.md` | 전체 내용 |
| 7 | `docs/issues/phase7-static-files.md` | 전체 내용 |
| 8 | `docs/issues/phase8-security.md` | 전체 내용 |
| 9 | `docs/issues/phase9-testing.md` | 전체 내용 |
| 10 | `docs/issues/phase10-documentation.md` | 전체 내용 |

**4. 이슈 작성**

각 Phase마다:
1. Title에서 `# ` 부분을 제외한 제목 입력
   - 예: `Phase 1: 프로젝트 초기 설정`
2. Description에 파일 내용 전체를 붙여넣기
3. Labels 추가 (파일 하단에 표시된 레이블)
   - Phase 1: `setup`, `phase-1`, `priority-high`
   - Phase 2: `feature`, `phase-2`, `priority-high`
   - 등등...
4. "Submit new issue" 클릭

---

## 📋 빠른 체크리스트

이슈 생성 전 확인사항:

- [ ] Phase 1 이슈 생성
- [ ] Phase 2 이슈 생성
- [ ] Phase 3 이슈 생성
- [ ] Phase 4 이슈 생성
- [ ] Phase 5 이슈 생성
- [ ] Phase 6 이슈 생성
- [ ] Phase 7 이슈 생성
- [ ] Phase 8 이슈 생성
- [ ] Phase 9 이슈 생성
- [ ] Phase 10 이슈 생성

---

## 💡 팁: VS Code에서 빠르게 복사하기

1. VS Code 탐색기에서 `docs/issues/` 폴더 열기
2. 각 `.md` 파일 열기
3. `Ctrl+A` (전체 선택) → `Ctrl+C` (복사)
4. GitHub 이슈 페이지에서 `Ctrl+V` (붙여넣기)

---

## 🎯 예상 소요 시간

수동으로 10개 이슈 생성: **약 10-15분**

---

## ❓ 여전히 문제가 있나요?

다음 사항을 확인하세요:

1. **Token 권한 확인**
   - https://github.com/settings/tokens
   - 해당 토큰의 `repo` 권한이 체크되어 있는지 확인

2. **리포지토리 권한 확인**
   - 본인이 리포지토리의 소유자인지 확인
   - Collaborator 권한이 있는지 확인

3. **Token 만료 확인**
   - 토큰 만료 날짜 확인
   - 필요시 새 토큰 생성

---

**이제 위의 옵션 2를 따라 수동으로 이슈를 생성해주세요!** 

파일들은 모두 `docs/issues/` 폴더에 준비되어 있습니다. 🎉

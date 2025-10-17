# 메모짱 프로젝트 이슈 템플릿

이 디렉토리에는 "메모짱" Django 프로젝트를 구현하기 위한 10개의 Phase별 이슈 템플릿이 포함되어 있습니다.

## 이슈 목록

1. **Phase 1: 프로젝트 초기 설정** (`phase1-project-setup.md`)
   - 가상환경, Django 설치, 프로젝트 구조 생성
   - 예상 소요: 1-2일

2. **Phase 2: Django 앱 생성 및 설정** (`phase2-django-apps.md`)
   - Users 앱, Memos 앱 생성 및 기본 설정
   - 예상 소요: 1-2일

3. **Phase 3: 데이터베이스 설정** (`phase3-database-setup.md`)
   - 마이그레이션, Admin 페이지 설정
   - 예상 소요: 1일

4. **Phase 4: URL 라우팅 설정** (`phase4-url-routing.md`)
   - URL 패턴 정의 및 구조화
   - 예상 소요: 1일

5. **Phase 5: 템플릿 개발** (`phase5-template-development.md`)
   - HTML 템플릿, Bootstrap UI 구현
   - 예상 소요: 2-3일

6. **Phase 6: Views 및 로직 구현** (`phase6-views-logic.md`)
   - 비즈니스 로직, CRUD 기능 구현
   - 예상 소요: 2-3일

7. **Phase 7: 정적 파일 및 스타일링** (`phase7-static-files.md`)
   - CSS, JavaScript, 커스텀 스타일
   - 예상 소요: 1일

8. **Phase 8: 보안 및 인증 강화** (`phase8-security.md`)
   - 보안 설정, 권한 검증
   - 예상 소요: 1일

9. **Phase 9: 테스트 작성** (`phase9-testing.md`)
   - 단위 테스트, 통합 테스트
   - 예상 소요: 2일

10. **Phase 10: 문서화 및 배포 준비** (`phase10-documentation.md`)
    - README, API 문서, 배포 설정
    - 예상 소요: 1일

## GitHub Issues 생성 방법

### 방법 1: 자동 스크립트 사용 (권장)

1. GitHub Personal Access Token 생성
   - https://github.com/settings/tokens 접속
   - "Generate new token (classic)" 클릭
   - `repo` 권한 체크
   - 토큰 생성 및 복사

2. 환경 변수 설정
   ```powershell
   $env:GITHUB_TOKEN = "your_personal_access_token"
   ```

3. 스크립트 실행
   ```powershell
   .\create-issues.ps1
   ```

### 방법 2: 수동으로 생성

각 마크다운 파일의 내용을 복사하여 GitHub Issues 페이지에서 직접 생성:

1. https://github.com/Seungchul-Kang/kwinfe-test/issues/new 접속
2. 해당 Phase의 마크다운 파일 내용 복사
3. Title과 Description 입력
4. Labels 추가 (각 파일 하단에 명시됨)
5. "Submit new issue" 클릭

## 프로젝트 진행 순서

Phase는 순차적으로 진행하는 것을 권장합니다:

```
Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5
                                              ↓
Phase 10 ← Phase 9 ← Phase 8 ← Phase 7 ← Phase 6
```

일부 Phase는 병렬로 진행 가능:
- Phase 4와 Phase 5는 부분적으로 병렬 가능
- Phase 7은 Phase 5 이후 언제든 가능

## 총 예상 기간

**약 2주** (11-14일)

## 주의사항

- 각 Phase 완료 후 커밋 및 푸시 권장
- 테스트를 주기적으로 실행하여 오류 조기 발견
- 코딩 규칙(python.instructions.md, database.instructions.md) 준수
- 보안 체크리스트 항상 확인

## 문의

이슈 생성 또는 프로젝트 진행 중 문제가 있으면 GitHub Issues에 질문을 남겨주세요.

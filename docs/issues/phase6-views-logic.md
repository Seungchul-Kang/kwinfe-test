# Phase 6: Views 및 로직 구현

## 설명
비즈니스 로직과 뷰 기능을 구현합니다.

## 작업 내용

### 6.1 Users 뷰 구현
- [ ] 회원가입 뷰
  - `UserCreationForm` 확장하여 이메일 필드 추가
  - 회원가입 성공 시 자동 로그인
  - 성공 메시지 표시
- [ ] 로그인 뷰
  - Django 내장 `LoginView` 활용
  - `LOGIN_REDIRECT_URL` 설정
- [ ] 로그아웃 뷰
  - Django 내장 `LogoutView` 활용
  - `LOGOUT_REDIRECT_URL` 설정
- [ ] 로그인 필수 데코레이터 적용

### 6.2 Memos 뷰 구현
- [ ] 메모 목록 뷰
  - `LoginRequiredMixin` + `ListView`
  - 현재 사용자의 메모만 필터링
  - 페이지네이션 적용 (선택 사항)
- [ ] 메모 생성 뷰
  - `LoginRequiredMixin` + `CreateView`
  - 자동으로 현재 사용자를 user 필드에 설정
  - 생성 성공 메시지
- [ ] 메모 상세 뷰
  - `LoginRequiredMixin` + `DetailView`
  - 소유자 확인 (본인 메모만 조회)
- [ ] 메모 수정 뷰
  - `LoginRequiredMixin` + `UpdateView`
  - 소유자 확인 (본인 메모만 수정)
  - 수정 성공 메시지
- [ ] 메모 삭제 뷰
  - `LoginRequiredMixin` + `DeleteView`
  - 소유자 확인 (본인 메모만 삭제)
  - 삭제 성공 메시지

### 6.3 권한 검증 로직
- [ ] `get_queryset()` 메서드 오버라이드
- [ ] 사용자별 메모 필터링
- [ ] 타 사용자 메모 접근 시 403 오류 또는 리다이렉트

## 완료 조건
- 모든 뷰가 정상적으로 동작함
- 인증되지 않은 사용자는 로그인 페이지로 리다이렉트됨
- 사용자는 자신의 메모만 CRUD 가능
- 성공/오류 메시지가 적절히 표시됨
- Python 코딩 규칙을 준수함

## 의존성
- Phase 3, 5 완료 필요

## 예상 소요 시간
2-3일

## Labels
`backend`, `views`, `phase-6`, `priority-high`

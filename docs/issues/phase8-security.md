# Phase 8: 보안 및 인증 강화

## 설명
보안 설정을 강화하고 인증 시스템을 개선합니다.

## 작업 내용

### 8.1 보안 설정
- [ ] `settings.py` 보안 설정 확인
  - `CSRF_COOKIE_SECURE` (프로덕션)
  - `SESSION_COOKIE_SECURE` (프로덕션)
  - `SECURE_SSL_REDIRECT` (프로덕션)
  - `SECURE_BROWSER_XSS_FILTER`
  - `X_FRAME_OPTIONS`
- [ ] `LOGIN_URL` 설정
- [ ] `LOGIN_REDIRECT_URL` 설정
- [ ] `LOGOUT_REDIRECT_URL` 설정
- [ ] 비밀번호 유효성 검사 강화
  - 최소 길이
  - 복잡도 요구사항

### 8.2 권한 검증
- [ ] 각 뷰에서 사용자 권한 확인
- [ ] `get_queryset()` 메서드로 사용자별 데이터 필터링
- [ ] 타 사용자 리소스 접근 시 적절한 오류 처리
- [ ] CSRF 토큰 모든 폼에 적용 확인

### 8.3 입력값 검증
- [ ] 폼 필드 유효성 검사
- [ ] XSS 공격 방어
- [ ] SQL Injection 방어 (Django ORM 사용으로 기본 제공)
- [ ] 파일 업로드 검증 (향후 기능 추가 시)

### 8.4 환경 변수 관리
- [ ] `.env` 파일에 모든 시크릿 정보 저장
- [ ] `SECRET_KEY` 환경 변수로 관리
- [ ] 데이터베이스 연결 정보 환경 변수로 관리
- [ ] `.env.example` 파일 생성

## 보안 체크리스트
- [ ] 하드코딩된 시크릿 없음
- [ ] 모든 폼에 CSRF 토큰 적용
- [ ] 인증되지 않은 사용자 접근 제한
- [ ] 사용자별 데이터 격리
- [ ] 적절한 오류 메시지 (민감 정보 노출 방지)

## 완료 조건
- 모든 보안 설정이 적절히 구성됨
- 환경 변수가 안전하게 관리됨
- 권한 검증이 모든 뷰에 적용됨
- 보안 취약점이 없음

## 의존성
- Phase 6 완료 필요

## 예상 소요 시간
1일

## Labels
`security`, `phase-8`, `priority-high`

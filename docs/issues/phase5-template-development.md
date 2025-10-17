# Phase 5: 템플릿 개발

## 설명
Django 템플릿을 사용하여 프론트엔드 UI를 구현합니다.

## 작업 내용

### 5.1 베이스 템플릿 생성
- [ ] `templates/base.html` 생성
  - Bootstrap CDN 추가
  - 네비게이션 바 (로그인/로그아웃, 메모 목록 링크)
  - 메시지 표시 영역
  - 푸터
  - 블록(block) 정의: `{% block content %}`

### 5.2 사용자 템플릿
- [ ] `templates/users/login.html`
  - 로그인 폼
  - 회원가입 링크
- [ ] `templates/users/register.html`
  - 회원가입 폼
  - 로그인 링크

### 5.3 메모 템플릿
- [ ] `templates/memos/memo_list.html`
  - 메모 목록 (카드 형식)
  - 메모 생성 버튼
  - 검색 기능 (선택 사항)
- [ ] `templates/memos/memo_detail.html`
  - 메모 상세 정보
  - 수정/삭제 버튼
- [ ] `templates/memos/memo_form.html`
  - 메모 생성/수정 폼
  - django-crispy-forms 활용
- [ ] `templates/memos/memo_confirm_delete.html`
  - 삭제 확인 페이지

### 5.4 홈페이지 템플릿
- [ ] `templates/home.html`
  - 환영 메시지
  - 로그인/회원가입 버튼 (비로그인 시)
  - 메모 목록 바로가기 (로그인 시)

## UI 요구사항
- 반응형 디자인 (Bootstrap 활용)
- 일관된 디자인 패턴
- 사용자 친화적인 인터페이스
- 메시지 알림 표시 (성공, 오류, 경고)

## 완료 조건
- 모든 템플릿이 생성되고 base.html을 상속받음
- Bootstrap이 정상적으로 적용됨
- 모든 페이지가 반응형으로 동작함
- django-crispy-forms가 폼 스타일링에 적용됨

## 의존성
- Phase 2, 4 완료 필요

## 예상 소요 시간
2-3일

## Labels
`frontend`, `templates`, `phase-5`, `priority-high`

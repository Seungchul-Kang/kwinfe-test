# Phase 4: URL 라우팅 설정

## 설명
프로젝트의 URL 구조를 설계하고 각 앱의 URL 패턴을 설정합니다.

## 작업 내용

### 4.1 메인 URL 설정
- [ ] `memojjang/urls.py` 수정
  - Admin URL 패턴
  - 홈페이지 URL 패턴 (`/`)
  - Users 앱 URL 포함 (`/users/`)
  - Memos 앱 URL 포함 (`/memos/`)

### 4.2 Users 앱 URL 설정
- [ ] `apps/users/urls.py` 생성
  - 로그인: `/users/login/`
  - 회원가입: `/users/register/`
  - 로그아웃: `/users/logout/`

### 4.3 Memos 앱 URL 설정
- [ ] `apps/memos/urls.py` 생성
  - 메모 목록: `/memos/`
  - 메모 생성: `/memos/create/`
  - 메모 상세: `/memos/<pk>/`
  - 메모 수정: `/memos/<pk>/edit/`
  - 메모 삭제: `/memos/<pk>/delete/`

## URL 구조
```
/                           - 홈페이지
/admin/                     - Admin 페이지
/users/login/               - 로그인
/users/register/            - 회원가입
/users/logout/              - 로그아웃
/memos/                     - 메모 목록
/memos/create/              - 메모 생성
/memos/<pk>/                - 메모 상세
/memos/<pk>/edit/           - 메모 수정
/memos/<pk>/delete/         - 메모 삭제
```

## 완료 조건
- 모든 URL 패턴이 정의됨
- URL 이름(name)이 명확하게 지정됨
- URL 패턴이 RESTful 규칙을 따름

## 의존성
- Phase 2 완료 필요

## 예상 소요 시간
1일

## Labels
`configuration`, `phase-4`, `priority-medium`

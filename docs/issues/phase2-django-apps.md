# Phase 2: Django 앱 생성 및 설정

## 설명
Users 앱과 Memos 앱을 생성하고 기본 구조를 설정합니다.

## 작업 내용

### 2.1 Users 앱 생성
- [ ] `users` 앱 생성 (`apps/users`)
- [ ] `models.py`: Django 기본 User 모델 확장 (필요시)
- [ ] `forms.py`: 회원가입, 로그인 폼 생성
- [ ] `views.py`: 회원가입, 로그인, 로그아웃 뷰 구현
- [ ] `urls.py`: URL 패턴 정의
- [ ] `settings.py`: `INSTALLED_APPS`에 `apps.users` 추가

### 2.2 Memos 앱 생성
- [ ] `memos` 앱 생성 (`apps/memos`)
- [ ] `models.py`: Memo 모델 정의
  - `user` (ForeignKey)
  - `title` (TextField)
  - `content` (TextField)
  - `created_at` (DateTimeField)
  - `updated_at` (DateTimeField)
- [ ] `forms.py`: 메모 작성/수정 폼 생성
- [ ] `views.py`: CRUD 뷰 구현
  - ListView, DetailView, CreateView, UpdateView, DeleteView
- [ ] `urls.py`: URL 패턴 정의
- [ ] `settings.py`: `INSTALLED_APPS`에 `apps.memos` 추가

## 완료 조건
- Users 앱과 Memos 앱이 생성되고 `INSTALLED_APPS`에 등록됨
- 각 앱의 models, forms, views, urls 파일이 기본 구조로 작성됨
- 코드가 Python 코딩 규칙을 준수함

## 의존성
- Phase 1 완료 필요

## 예상 소요 시간
1-2일

## Labels
`feature`, `phase-2`, `priority-high`

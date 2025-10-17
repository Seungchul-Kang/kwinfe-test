# Phase 1: 프로젝트 초기 설정

## 설명
Django 프로젝트의 기본 환경을 구성하고 초기 프로젝트 구조를 생성합니다.

## 작업 내용

### 1.1 개발 환경 구성
- [ ] Python 가상환경 생성 및 활성화
- [ ] Django 및 필수 패키지 설치
  - `django`
  - `django-crispy-forms`
  - `crispy-bootstrap4`
  - `python-decouple`
- [ ] `requirements.txt` 생성

### 1.2 Django 프로젝트 생성
- [ ] Django 프로젝트 `memojjang` 생성
- [ ] 디렉토리 구조 생성
  ```
  apps/
  db/
  static/css/
  static/js/
  templates/
  templates/memos/
  templates/users/
  docs/
  ```

### 1.3 환경 변수 설정
- [ ] `.env` 파일 생성
  - `SECRET_KEY`
  - `DEBUG`
  - `DATABASE_URL`
- [ ] `.gitignore` 파일 생성
  - `.env`
  - `db.sqlite3`
  - `__pycache__/`
  - `*.pyc`
  - `venv/`
  - `staticfiles/`

## 완료 조건
- 가상환경이 활성화되고 모든 필수 패키지가 설치됨
- Django 프로젝트가 생성되고 기본 서버 실행 가능
- 환경 변수가 `.env` 파일로 관리됨
- `.gitignore`가 적절히 설정됨

## 예상 소요 시간
1-2일

## Labels
`setup`, `phase-1`, `priority-high`

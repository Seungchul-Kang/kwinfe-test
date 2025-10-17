# Phase 3: 데이터베이스 설정

## 설명
데이터베이스 모델을 마이그레이션하고 Admin 페이지를 설정합니다.

## 작업 내용

### 3.1 모델 마이그레이션
- [ ] Users 앱 마이그레이션 파일 생성
  ```bash
  python manage.py makemigrations users
  ```
- [ ] Memos 앱 마이그레이션 파일 생성
  ```bash
  python manage.py makemigrations memos
  ```
- [ ] 마이그레이션 실행
  ```bash
  python manage.py migrate
  ```
- [ ] 슈퍼유저 생성
  ```bash
  python manage.py createsuperuser
  ```

### 3.2 Admin 페이지 설정
- [ ] `apps/users/admin.py`: User 모델 등록
- [ ] `apps/memos/admin.py`: Memo 모델 등록
  - 목록에 표시할 필드 설정 (list_display)
  - 검색 필드 설정 (search_fields)
  - 필터 설정 (list_filter)

## 완료 조건
- 모든 마이그레이션이 성공적으로 실행됨
- SQLite 데이터베이스 파일(`db.sqlite3`)이 `db/` 디렉토리에 생성됨
- Admin 페이지에서 User와 Memo 모델을 관리할 수 있음
- 데이터베이스 스키마가 database.instructions.md의 규칙을 준수함

## 의존성
- Phase 2 완료 필요

## 예상 소요 시간
1일

## Labels
`database`, `phase-3`, `priority-high`

# 슈퍼유저 생성 가이드

## 슈퍼유저 생성 방법

Django 관리자 페이지에 접근하려면 슈퍼유저 계정이 필요합니다.

### 명령어

```bash
python manage.py createsuperuser
```

### 입력 정보

1. **Username (사용자명)**: 관리자 계정 이름
2. **Email (이메일)**: 관리자 이메일 (선택사항)
3. **Password (비밀번호)**: 8자 이상의 안전한 비밀번호

### 예시

```
Username: admin
Email address: admin@example.com
Password: ********
Password (again): ********
Superuser created successfully.
```

### Admin 페이지 접속

서버 실행 후:
- URL: http://127.0.0.1:8000/admin/
- 생성한 슈퍼유저 계정으로 로그인

# 🔍 비밀번호 재설정 이메일 문제 해결 가이드

## 📋 문제 진단

콘솔에 이메일이 출력되지 않는 이유는 다음 중 하나일 수 있습니다:

### 1. 서버가 재시작되지 않음
- 설정을 변경한 후 서버를 재시작해야 합니다.

### 2. 사용자에게 이메일이 등록되어 있지 않음
- Django는 이메일이 등록된 사용자에게만 비밀번호 재설정 이메일을 보냅니다.
- 이메일이 없는 사용자는 조용히 무시됩니다 (보안상의 이유).

### 3. 가상환경이 활성화되지 않음
- Python 명령 실행 시 가상환경의 Python을 사용해야 합니다.

---

## 🔧 해결 방법

### 방법 1: 테스트 스크립트 실행

```powershell
# 테스트 스크립트 실행
.\.venv\Scripts\python.exe test_password_reset.py
```

이 스크립트는:
- ✅ 이메일 설정 확인
- ✅ 테스트 이메일 전송 (콘솔 출력)
- ✅ 등록된 사용자 및 이메일 확인

---

### 방법 2: 서버 재시작 및 테스트

#### Step 1: 서버 실행
```powershell
.\.venv\Scripts\python.exe manage.py runserver
```

#### Step 2: 이메일이 있는 사용자로 회원가입
1. http://127.0.0.1:8000/users/register/ 접속
2. **이메일 주소를 꼭 입력**하여 회원가입
3. 로그아웃

#### Step 3: 비밀번호 재설정 테스트
1. http://127.0.0.1:8000/users/login/ 접속
2. "비밀번호를 잊으셨나요?" 클릭
3. 가입 시 입력한 **정확한 이메일 주소** 입력
4. "재설정 링크 전송" 버튼 클릭
5. **서버가 실행 중인 터미널/콘솔 확인** ⭐

#### Step 4: 콘솔 출력 예시
```
[28/Oct/2025 14:30:15] "POST /users/password-reset/ HTTP/1.1" 302 0
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Subject: 비밀번호 재설정 요청
From: noreply@memojjang.com
To: user@example.com
Date: ...

안녕하세요, testuser님!

메모짱에서 비밀번호 재설정을 요청하셨습니다.

아래 링크를 클릭하여 새로운 비밀번호를 설정해주세요:

http://127.0.0.1:8000/users/password-reset-confirm/...
...
```

---

### 방법 3: Admin에서 이메일 추가

기존 사용자에게 이메일을 추가하려면:

```powershell
# 슈퍼유저 생성 (아직 없다면)
.\.venv\Scripts\python.exe manage.py createsuperuser

# 서버 실행
.\.venv\Scripts\python.exe manage.py runserver
```

1. http://127.0.0.1:8000/admin/ 접속
2. Users → 사용자 선택
3. Email address 입력 후 저장

---

## 🎯 빠른 테스트 (권장)

### 1. 테스트 스크립트로 설정 확인
```powershell
.\.venv\Scripts\python.exe test_password_reset.py
```

### 2. 이메일 출력 확인
- ✅ "✅ 이메일이 콘솔에 출력되었어야 합니다!" 메시지 표시
- ✅ 콘솔에 이메일 내용이 출력됨

### 3. 등록된 사용자 확인
- 이메일이 있는 사용자가 있는지 확인
- 없다면 새로 회원가입 (이메일 필수 입력)

---

## ⚠️ 주의사항

### Django의 비밀번호 재설정 보안 정책

Django는 보안상의 이유로 다음과 같이 동작합니다:

1. **존재하지 않는 이메일**: 조용히 무시 (오류 메시지 없음)
2. **이메일이 없는 사용자**: 조용히 무시
3. **성공 메시지는 항상 표시**: 실제 이메일 전송 여부와 관계없이

**왜?** 공격자가 등록된 이메일인지 확인하는 것을 방지하기 위함

따라서:
- ✅ "이메일 전송 완료" 페이지가 표시되어도
- ❌ 실제로 이메일이 전송되지 않을 수 있음

**해결책**: 
- 반드시 **이메일이 등록된 사용자**로 테스트
- 서버 콘솔에서 실제 이메일 출력 확인

---

## 🐛 여전히 문제가 있나요?

다음 정보를 확인해주세요:

```powershell
# 1. Django 버전 확인
.\.venv\Scripts\python.exe -m django --version

# 2. 설정 확인
.\.venv\Scripts\python.exe manage.py shell
>>> from django.conf import settings
>>> print(settings.EMAIL_BACKEND)
>>> exit()

# 3. 사용자 확인
.\.venv\Scripts\python.exe manage.py shell
>>> from django.contrib.auth.models import User
>>> for u in User.objects.all():
...     print(f"{u.username}: {u.email}")
>>> exit()
```

---

## 💡 정상 작동 확인 방법

1. ✅ 테스트 스크립트 실행 시 콘솔에 이메일 출력
2. ✅ 비밀번호 재설정 요청 시 서버 콘솔에 이메일 내용 표시
3. ✅ 이메일의 링크로 접속 시 비밀번호 변경 페이지 표시
4. ✅ 새 비밀번호로 로그인 성공

---

**문제가 해결되지 않으면 `test_password_reset.py` 실행 결과를 공유해주세요!** 📧

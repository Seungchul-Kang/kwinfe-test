# 메모짱 (Memojjang)

Django 기반의 간편한 메모 웹 애플리케이션

## 프로젝트 소개

메모짱은 사용자가 간편하게 메모를 작성, 관리할 수 있는 웹 애플리케이션입니다. 
사용자 인증 시스템을 통해 각 사용자의 메모를 안전하게 보관하고 관리할 수 있습니다.

## 주요 기능

- ✅ 사용자 회원가입 및 로그인
- ✅ 메모 작성, 수정, 삭제
- ✅ 메모 목록 조회 (본인 메모만)
- ✅ 반응형 웹 디자인 (모바일 지원)
- ✅ 사용자별 메모 격리 (보안)

## 기술 스택

### 백엔드
- **Django 5.2.7**: Python 웹 프레임워크
- **SQLite**: 데이터베이스
- **Python 3.14.0**: 프로그래밍 언어

### 프론트엔드
- **Django Templates**: 템플릿 엔진
- **Bootstrap 5.3.0**: UI 프레임워크
- **Bootstrap Icons**: 아이콘
- **JavaScript**: 클라이언트 사이드 스크립팅

### 주요 라이브러리
- `django-crispy-forms`: 폼 스타일링
- `crispy-bootstrap4`: Bootstrap 4 템플릿 팩
- `python-decouple`: 환경 변수 관리

## 설치 및 실행

### 1. 저장소 클론

```bash
git clone https://github.com/Seungchul-Kang/kwinfe-test.git
cd kwinfe-test
```

### 2. 가상환경 생성 및 활성화

```bash
# Windows
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. 패키지 설치

```bash
pip install -r requirements.txt
```

### 4. 환경 변수 설정

`.env.example` 파일을 복사하여 `.env` 파일을 생성하고 필요한 값을 설정합니다.

```bash
# Windows
copy .env.example .env

# macOS/Linux
cp .env.example .env
```

### 5. 데이터베이스 마이그레이션

```bash
python manage.py migrate
```

### 6. 슈퍼유저 생성 (선택사항)

```bash
python manage.py createsuperuser
```

### 7. 개발 서버 실행

```bash
python manage.py runserver
```

브라우저에서 http://127.0.0.1:8000/ 접속

## 프로젝트 구조

```
kwinfe-test/
├── .github/              # GitHub 설정 및 지침
│   ├── copilot-instructions.md
│   └── instructions/
├── apps/                 # Django 앱들
│   ├── memos/           # 메모 앱
│   │   ├── models.py    # Memo 모델
│   │   ├── views.py     # CRUD 뷰
│   │   ├── forms.py     # 메모 폼
│   │   └── urls.py      # URL 패턴
│   └── users/           # 사용자 앱
│       ├── views.py     # 인증 뷰
│       ├── forms.py     # 사용자 폼
│       └── urls.py      # URL 패턴
├── db/                  # 데이터베이스 파일
│   └── db.sqlite3      
├── docs/                # 문서
│   ├── issues/         # 이슈 템플릿
│   ├── SUPERUSER_GUIDE.md
│   └── URL_STRUCTURE.md
├── memojjang/           # Django 프로젝트 설정
│   ├── settings.py     # 프로젝트 설정
│   ├── urls.py         # 메인 URL 설정
│   └── wsgi.py         
├── static/              # 정적 파일
│   ├── css/            # CSS 파일
│   └── js/             # JavaScript 파일
├── templates/           # Django 템플릿
│   ├── base.html       # 기본 템플릿
│   ├── home.html       # 홈페이지
│   ├── memos/          # 메모 템플릿
│   └── users/          # 사용자 템플릿
├── .env.example         # 환경 변수 예제
├── .gitignore          
├── manage.py           
└── requirements.txt     # Python 패키지 목록
```

## 사용 방법

### 1. 회원가입
- 홈페이지에서 "회원가입" 버튼 클릭
- 사용자명, 이메일, 비밀번호 입력
- 자동으로 로그인됨

### 2. 메모 작성
- 로그인 후 "새 메모 작성" 버튼 클릭
- 제목과 내용 입력
- "작성하기" 버튼 클릭

### 3. 메모 관리
- **목록 보기**: "내 메모" 메뉴에서 모든 메모 조회
- **상세 보기**: 메모 카드 클릭
- **수정**: 상세 페이지에서 "수정" 버튼
- **삭제**: 상세 페이지에서 "삭제" 버튼 (확인 필요)

## URL 구조

| URL | 기능 | 인증 필요 |
|-----|------|----------|
| `/` | 홈페이지 | No |
| `/admin/` | 관리자 페이지 | Yes (Staff) |
| `/users/register/` | 회원가입 | No |
| `/users/login/` | 로그인 | No |
| `/users/logout/` | 로그아웃 | Yes |
| `/memos/` | 메모 목록 | Yes |
| `/memos/create/` | 메모 작성 | Yes |
| `/memos/<pk>/` | 메모 상세 | Yes |
| `/memos/<pk>/edit/` | 메모 수정 | Yes |
| `/memos/<pk>/delete/` | 메모 삭제 | Yes |

자세한 내용은 [URL_STRUCTURE.md](docs/URL_STRUCTURE.md) 참조

## 개발 가이드

### 코딩 컨벤션
- Python: `.github/instructions/python.instructions.md` 참조
- 데이터베이스: `.github/instructions/database.instructions.md` 참조
- 테스트: `.github/instructions/test.instructions.md` 참조

### 테스트 실행

```bash
python manage.py test
```

### 정적 파일 수집 (배포용)

```bash
python manage.py collectstatic
```

## 보안 고려사항

- ✅ CSRF 보호 활성화
- ✅ 사용자별 데이터 격리
- ✅ 비밀번호 해싱 (Django 기본)
- ✅ SQL Injection 방어 (Django ORM)
- ✅ XSS 방어 (Django 템플릿 자동 이스케이프)
- ✅ 환경 변수로 시크릿 관리

## 라이선스

이 프로젝트는 교육 목적으로 작성되었습니다.

## 기여자

- Seungchul-Kang ([@Seungchul-Kang](https://github.com/Seungchul-Kang))

## 문의

프로젝트 관련 문의사항은 GitHub Issues에 등록해주세요.

---

**메모짱** - 간편하고 안전한 메모 관리 💡

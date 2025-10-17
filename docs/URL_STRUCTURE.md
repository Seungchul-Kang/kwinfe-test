# 메모짱 URL 구조

## URL 패턴 목록

### 홈페이지
- **URL**: `/`
- **이름**: `home`
- **설명**: 메인 홈페이지 (환영 메시지)

### Admin (관리자 페이지)
- **URL**: `/admin/`
- **설명**: Django 관리자 페이지

### Users (사용자 관련)
- **기본 경로**: `/users/`

| URL | 이름 | 설명 | 인증 필요 |
|-----|------|------|----------|
| `/users/register/` | `users:register` | 회원가입 | No |
| `/users/login/` | `users:login` | 로그인 | No |
| `/users/logout/` | `users:logout` | 로그아웃 | Yes |

### Memos (메모 관련)
- **기본 경로**: `/memos/`

| URL | 이름 | 설명 | 인증 필요 | 권한 |
|-----|------|------|----------|------|
| `/memos/` | `memos:list` | 메모 목록 | Yes | 본인 메모만 |
| `/memos/create/` | `memos:create` | 메모 생성 | Yes | - |
| `/memos/<pk>/` | `memos:detail` | 메모 상세 | Yes | 본인 메모만 |
| `/memos/<pk>/edit/` | `memos:edit` | 메모 수정 | Yes | 본인 메모만 |
| `/memos/<pk>/delete/` | `memos:delete` | 메모 삭제 | Yes | 본인 메모만 |

## 리다이렉션 설정

### 로그인 관련
- **LOGIN_URL**: `users:login`
- **LOGIN_REDIRECT_URL**: `memos:list`
  - 로그인 성공 후 메모 목록으로 이동
- **LOGOUT_REDIRECT_URL**: `home`
  - 로그아웃 후 홈페이지로 이동

## URL 네이밍 규칙

- **앱 네임스페이스**: `users`, `memos`
- **사용 방법**: 
  - 템플릿: `{% url 'memos:list' %}`
  - 뷰/코드: `reverse('memos:list')`

## 예제 사용법

### 템플릿에서 URL 사용
```django
<!-- 메모 목록 링크 -->
<a href="{% url 'memos:list' %}">메모 목록</a>

<!-- 메모 상세 링크 -->
<a href="{% url 'memos:detail' memo.pk %}">{{ memo.title }}</a>

<!-- 로그인 링크 -->
<a href="{% url 'users:login' %}">로그인</a>
```

### 뷰에서 URL 리다이렉트
```python
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect

# redirect 사용
return redirect('memos:list')

# reverse 사용
url = reverse('memos:detail', kwargs={'pk': memo.pk})

# reverse_lazy 사용 (클래스 기반 뷰)
success_url = reverse_lazy('memos:list')
```

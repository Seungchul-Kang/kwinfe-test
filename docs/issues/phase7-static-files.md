# Phase 7: 정적 파일 및 스타일링

## 설명
CSS, JavaScript 등 정적 파일을 작성하고 UI를 개선합니다.

## 작업 내용

### 7.1 CSS 파일 생성
- [ ] `static/css/main.css` 생성
  - 커스텀 스타일 작성
  - 색상 테마 정의
  - 간격, 폰트 등 일관성 있게 설정
- [ ] Bootstrap 테마 커스터마이징
  - 버튼 스타일
  - 카드 스타일
  - 폼 스타일

### 7.2 JavaScript (선택 사항)
- [ ] `static/js/main.js` 생성
  - 삭제 확인 모달
  - 폼 유효성 검사
  - 메모 검색 기능 (선택 사항)

### 7.3 settings.py 정적 파일 설정
- [ ] `STATIC_URL` 설정
- [ ] `STATICFILES_DIRS` 설정
- [ ] `STATIC_ROOT` 설정 (배포용)

### 7.4 템플릿에 정적 파일 적용
- [ ] `{% load static %}` 태그 추가
- [ ] CSS 파일 링크
- [ ] JavaScript 파일 링크

## UI/UX 개선 사항
- 반응형 디자인 최적화
- 버튼 호버 효과
- 폼 입력 필드 스타일링
- 로딩 인디케이터 (선택 사항)
- 애니메이션 효과 (선택 사항)

## 완료 조건
- 모든 정적 파일이 정상적으로 로드됨
- 커스텀 CSS가 적용되어 UI가 개선됨
- 모든 브라우저에서 일관된 스타일 표시
- 반응형 디자인이 모바일에서도 잘 작동함

## 의존성
- Phase 5 완료 필요

## 예상 소요 시간
1일

## Labels
`frontend`, `css`, `javascript`, `phase-7`, `priority-medium`

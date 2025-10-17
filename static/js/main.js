// 메모짱 JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // 알림 메시지 자동 숨김
    const alerts = document.querySelectorAll('.alert:not(.alert-danger)');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // 삭제 확인 모달 (추가 보안)
    const deleteButtons = document.querySelectorAll('a[href*="/delete/"]');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            // 삭제 페이지로 이동하므로 추가 확인은 불필요
            // 필요시 여기에 confirm() 추가 가능
        });
    });

    // 폼 제출 시 버튼 비활성화 (중복 제출 방지)
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const submitButton = form.querySelector('button[type="submit"]');
            if (submitButton) {
                submitButton.disabled = true;
                submitButton.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>처리 중...';
            }
        });
    });

    // 텍스트 영역 자동 높이 조절
    const textareas = document.querySelectorAll('textarea');
    textareas.forEach(textarea => {
        textarea.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = (this.scrollHeight) + 'px';
        });
    });

    // 네비게이션 드롭다운 호버 효과 (데스크톱)
    if (window.innerWidth > 768) {
        const dropdowns = document.querySelectorAll('.dropdown');
        dropdowns.forEach(dropdown => {
            dropdown.addEventListener('mouseenter', function() {
                const dropdownMenu = this.querySelector('.dropdown-menu');
                if (dropdownMenu) {
                    dropdownMenu.classList.add('show');
                }
            });
            dropdown.addEventListener('mouseleave', function() {
                const dropdownMenu = this.querySelector('.dropdown-menu');
                if (dropdownMenu) {
                    dropdownMenu.classList.remove('show');
                }
            });
        });
    }

    // 스크롤 시 네비게이션 바 그림자 효과
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 10) {
            navbar.classList.add('shadow');
        } else {
            navbar.classList.remove('shadow');
        }
    });

    // 페이지 로드 시 포커스
    const autoFocus = document.querySelector('[autofocus]');
    if (autoFocus) {
        autoFocus.focus();
    }

    // 개발 모드 로그
    console.log('메모짱 JavaScript 로드 완료');
});

// 유틸리티 함수: 날짜 포맷팅
function formatDate(date) {
    const d = new Date(date);
    const year = d.getFullYear();
    const month = String(d.getMonth() + 1).padStart(2, '0');
    const day = String(d.getDate()).padStart(2, '0');
    const hours = String(d.getHours()).padStart(2, '0');
    const minutes = String(d.getMinutes()).padStart(2, '0');
    return `${year}-${month}-${day} ${hours}:${minutes}`;
}

// 유틸리티 함수: 문자열 자르기
function truncate(str, maxLength) {
    if (str.length <= maxLength) return str;
    return str.substring(0, maxLength) + '...';
}

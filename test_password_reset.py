"""
비밀번호 재설정 이메일 테스트 스크립트

실행 방법:
.\.venv\Scripts\python.exe test_password_reset.py
"""

import os
import django

# Django 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'memojjang.settings')
django.setup()

from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings

print("="*60)
print("비밀번호 재설정 이메일 테스트")
print("="*60)

# 설정 확인
print(f"\n1. EMAIL_BACKEND: {settings.EMAIL_BACKEND}")
print(f"2. DEFAULT_FROM_EMAIL: {settings.DEFAULT_FROM_EMAIL}")

# 테스트 이메일 전송
print("\n3. 테스트 이메일 전송 중...")
try:
    send_mail(
        subject='테스트 이메일',
        message='이것은 테스트 이메일입니다.',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=['test@example.com'],
        fail_silently=False,
    )
    print("✅ 이메일이 콘솔에 출력되었어야 합니다!")
except Exception as e:
    print(f"❌ 오류 발생: {e}")

# 사용자 확인
print("\n4. 등록된 사용자 확인:")
users = User.objects.all()
if users.exists():
    for user in users:
        print(f"   - {user.username} (이메일: {user.email or '없음'})")
else:
    print("   ⚠️  등록된 사용자가 없습니다!")

print("\n" + "="*60)
print("💡 팁: 비밀번호 재설정을 위해서는 사용자에게 이메일이 등록되어 있어야 합니다!")
print("="*60)

from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    
    # 비밀번호 변경 (로그인 필요)
    path('password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', views.UserPasswordChangeDoneView.as_view(), name='password_change_done'),
    
    # 테스트용 간단한 비밀번호 초기화 (인증 불필요) ⚠️
    path('simple-reset/', views.SimplePasswordResetView.as_view(), name='simple_reset'),
    
    # 비밀번호 재설정 (이메일 방식 - 백업용)
    path('password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', views.UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

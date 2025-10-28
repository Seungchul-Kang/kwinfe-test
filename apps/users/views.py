from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.views import (
    LoginView, 
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views import View
from django.utils.decorators import method_decorator
from .forms import UserRegisterForm, UserLoginForm


class UserRegisterView(CreateView):
    """회원가입 뷰"""
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('memos:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        # 회원가입 후 자동 로그인
        user = form.save()
        login(self.request, user)
        messages.success(self.request, f'{user.username}님, 환영합니다!')
        return response


class UserLoginView(LoginView):
    """로그인 뷰"""
    form_class = UserLoginForm
    template_name = 'users/login.html'

    def form_valid(self, form):
        messages.success(self.request, f'{form.get_user()}님, 환영합니다!')
        return super().form_valid(form)


class UserLogoutView(View):
    """로그아웃 뷰 - GET/POST 모두 처리"""
    
    def get(self, request):
        """GET 요청 시 로그아웃 확인 페이지 표시"""
        if request.user.is_authenticated:
            return render(request, 'users/logout_confirm.html')
        else:
            messages.info(request, '이미 로그아웃되어 있습니다.')
            return redirect('home')
    
    def post(self, request):
        """POST 요청 시 실제 로그아웃 처리"""
        if request.user.is_authenticated:
            username = request.user.username
            logout(request)
            messages.success(request, f'{username}님, 로그아웃되었습니다.')
        else:
            messages.info(request, '이미 로그아웃되어 있습니다.')
        return redirect('home')


class UserPasswordResetView(PasswordResetView):
    """비밀번호 재설정 요청 뷰"""
    template_name = 'users/password_reset_form.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject.txt'
    success_url = reverse_lazy('users:password_reset_done')
    
    def form_valid(self, form):
        messages.success(self.request, '비밀번호 재설정 링크가 이메일로 전송되었습니다.')
        return super().form_valid(form)


class UserPasswordResetDoneView(PasswordResetDoneView):
    """비밀번호 재설정 이메일 전송 완료 뷰"""
    template_name = 'users/password_reset_done.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    """비밀번호 재설정 확인 뷰"""
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')
    
    def form_valid(self, form):
        messages.success(self.request, '비밀번호가 성공적으로 변경되었습니다!')
        return super().form_valid(form)


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    """비밀번호 재설정 완료 뷰"""
    template_name = 'users/password_reset_complete.html'


class UserPasswordChangeView(PasswordChangeView):
    """로그인한 사용자의 비밀번호 변경 뷰"""
    template_name = 'users/password_change_form.html'
    success_url = reverse_lazy('users:password_change_done')
    
    def form_valid(self, form):
        messages.success(self.request, '비밀번호가 성공적으로 변경되었습니다!')
        return super().form_valid(form)


class UserPasswordChangeDoneView(View):
    """비밀번호 변경 완료 뷰"""
    
    def get(self, request):
        return render(request, 'users/password_change_done.html')

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    """사용자 회원가입 폼"""
    email = forms.EmailField(required=True, label='이메일')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': '사용자명',
            'password1': '비밀번호',
            'password2': '비밀번호 확인',
        }


class UserLoginForm(AuthenticationForm):
    """사용자 로그인 폼"""
    username = forms.CharField(label='사용자명')
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput)

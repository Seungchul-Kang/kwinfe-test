from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Memo
from .forms import MemoForm


class MemoListView(LoginRequiredMixin, ListView):
    """메모 목록 뷰"""
    model = Memo
    template_name = 'memos/memo_list.html'
    context_object_name = 'memos'
    paginate_by = 10

    def get_queryset(self):
        # 현재 사용자의 메모만 조회
        return Memo.objects.filter(user=self.request.user)


class MemoDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """메모 상세 뷰"""
    model = Memo
    template_name = 'memos/memo_detail.html'
    context_object_name = 'memo'

    def test_func(self):
        # 본인의 메모만 조회 가능
        memo = self.get_object()
        return self.request.user == memo.user


class MemoCreateView(LoginRequiredMixin, CreateView):
    """메모 생성 뷰"""
    model = Memo
    form_class = MemoForm
    template_name = 'memos/memo_form.html'

    def form_valid(self, form):
        # 자동으로 현재 사용자를 설정
        form.instance.user = self.request.user
        messages.success(self.request, '메모가 생성되었습니다.')
        return super().form_valid(form)


class MemoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """메모 수정 뷰"""
    model = Memo
    form_class = MemoForm
    template_name = 'memos/memo_form.html'

    def test_func(self):
        # 본인의 메모만 수정 가능
        memo = self.get_object()
        return self.request.user == memo.user

    def form_valid(self, form):
        messages.success(self.request, '메모가 수정되었습니다.')
        return super().form_valid(form)


class MemoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """메모 삭제 뷰"""
    model = Memo
    template_name = 'memos/memo_confirm_delete.html'
    success_url = reverse_lazy('memos:list')

    def test_func(self):
        # 본인의 메모만 삭제 가능
        memo = self.get_object()
        return self.request.user == memo.user

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, '메모가 삭제되었습니다.')
        return super().delete(request, *args, **kwargs)

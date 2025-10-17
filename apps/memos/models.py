from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Memo(models.Model):
    """메모 모델"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='memos', verbose_name='작성자')
    title = models.TextField(verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')

    class Meta:
        ordering = ['-created_at']
        verbose_name = '메모'
        verbose_name_plural = '메모 목록'

    def __str__(self):
        return f"{self.title[:50]}"

    def get_absolute_url(self):
        return reverse('memos:detail', kwargs={'pk': self.pk})

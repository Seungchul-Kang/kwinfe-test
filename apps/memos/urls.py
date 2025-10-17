from django.urls import path
from . import views

app_name = 'memos'

urlpatterns = [
    path('', views.MemoListView.as_view(), name='list'),
    path('create/', views.MemoCreateView.as_view(), name='create'),
    path('<int:pk>/', views.MemoDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.MemoUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.MemoDeleteView.as_view(), name='delete'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('article/', views.article_list, name='article_list'),
    path('article/new', views.article_new, name='article_new'),
    path('article/<pk>/edit', views.article_edit, name='article_edit'),
    path('article/<pk>/publish', views.article_publish, name='article_publish'),
    path('article/<pk>/delete', views.article_delete, name='article_delete'),
    path('<slug>', views.article_detail, name='article_delete'),
]

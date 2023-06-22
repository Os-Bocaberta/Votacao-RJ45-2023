from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('vote/', views.vote, name="vote"),
    path('result/', views.result, name="result"),
    path('post_datas', views.post_datas, name="post_datas")
]

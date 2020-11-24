from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_view),
    path('find/', views.find_view),
    path('regist/', views.regist_view),
]
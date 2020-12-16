from django.urls import path

from . import views

app_name = "Login"

urlpatterns = [
    path('', views.login_view,name = 'login'),
    path('find/', views.find_view,name = 'find'),
    path('regist/', views.regist_view,name = 'regist'),
    path('regist_post/',views.regist,name = 'regist_post'),
    path('login_post/',views.login,name = 'login_post'),
    path('logout_post/',views.logout,name = 'logout_post')
]
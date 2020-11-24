from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login_view(request):
    """
    登录主界面
    """
    return render(request,'Login/login_view.html')

def find_view(request):
    """
    找回界面
    """
    return render(request,'Login/find_view.html')

def regist_view(request):
    """
    注册界面
    """
    return render(request,'Login/regist_view.html')
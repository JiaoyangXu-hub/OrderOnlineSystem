from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators import csrf
from cmdb.models import Usr

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



Usr.get_deferred_fields
# 接收POST请求数据
def post_regist_form(request):
    """
    接收注册表单
    """
    if request.POST:
        if Usr.objects.filter(ID=request.POST['ID']):
            return HttpResponse("注册错误:用户名重复，请重新注册")
        else:
            # item = {k:None for k in ['ID','password','location','phoneNumber','email','stage']}
            item = request.POST.dict()
            item.pop('csrfmiddlewaretoken')
            item.update({'active':False})
            Usr.objects.create(**item)
        return render(request,"Login/login_view.html")
    else:
        return HttpResponse('注册错误:表单提交错误')

def post_find_form(request):
    """
    接收找回表单写入数据库
    """
    pass
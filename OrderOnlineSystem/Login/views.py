from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators import csrf
from cmdb.models import Usr
from Form import UsrForm,LoginForm

# from django.core.handlers.wsgi import WSGIRequest as request



# 加载指定页面

def login_view(request):
    """
    登录主界面
    """
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect(reverse(request.session['stage']+'System:base'))
        
    return render(request,'Login/login_view.html',{'form':LoginForm,'message':request.session.get('message','')})

def find_view(request):
    """
    找回界面
    """
    return render(request,'Login/find_view.html',{'form':UsrForm,'message':request.session.get('message','')})

def regist_view(request):
    """
    注册界面
    """
    return render(request,'Login/regist_view.html',{'form':UsrForm,'message':request.session.get('message','')})




def login(request):
    
    '''
    提交登录表单
    '''
    # request.session['is_login']=False

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            ID = login_form.cleaned_data.get('ID')
            password = login_form.cleaned_data.get('password')

            try:
                user = Usr.objects.get(ID=ID)
            except :
                request.session['message']='用户不存在！'
                return redirect('/Login/')
                # return render(request, 'Login/login_view.html', {"form":LoginForm,"message":message})

            if user.password == password:
                request.session.set_expiry(0)
                request.session['is_login'] = True   # 是否登录
                request.session['user_id'] = user.ID # 用户账号
                request.session['stage'] = user.stage# 用户身份
                return redirect(reverse(request.session['stage']+'System:base'))
            else:
                request.session['message'] = '密码不正确！'
                return redirect('/Login/')
                # return render(request, 'Login/login_view.html', {"form":LoginForm,"message":message})
        else:
            request.session['message'] = '填写格式不规范'
            return redirect('/Login/')
            # return render(request, 'Login/login_view.html', {"form":LoginForm,"message":message})
    else:
        request.session['message'] = '未知错误'
        return redirect('/Login/')
        # return render(request, 'Login/login_view.html', {"form":LoginForm,"message":message})

def logout(request):
    """
    在登录后进行退出登录 
    还没写路由什么的,只是定义了一个函数,具体退出需要在登录后的界面上安排
    """
    request.session['is_login']=False
    del request.session['user_id']
    del request.session['stage']
    request.session['message']=''
    return redirect('/Login/')

def regist(request):
    """
    提交注册表单动作
    """
    regist_form = UsrForm(request.POST)
    if regist_form.is_valid():# 检验完整性
        if Usr.objects.filter(ID = regist_form.clean().get('ID')):# 检验是否重复ID
            message = "账号已存在"
            return render(request, 'Login/regist_view.html',{"form":UsrForm,'message':message})
        else:
            tmp = regist_form.clean()
            Usr.objects.create(**tmp)
            return redirect('/Login/')
            # return render(request,'Login/login_view.html',{"form":LoginForm})

    elif regist_form.errors is not None:
        print(regist_form.errors)
        return HttpResponse(str(regist_form.errors))


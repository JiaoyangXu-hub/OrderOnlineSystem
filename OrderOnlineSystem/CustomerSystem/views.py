from django.shortcuts import render,redirect,HttpResponse
from cmdb.models import Menu


# Create your views here.

def base_view(request):
    """
    顾客主界面
    """
    if request.session['is_login']:
        menu = Menu.objects.all()
        user_id = request.session['user_id']
        return render(request,'C/base_view.html',{'menu':menu,'user_id':user_id})
    else:
        return redirect('/Login/')

def order_view(request):
    """
    订单详情
    """
    return render(request,'C/order_view.html')

def pay_view(request):
    """
    缴费详情
    """
    return render(request,'C/pay_view.html')
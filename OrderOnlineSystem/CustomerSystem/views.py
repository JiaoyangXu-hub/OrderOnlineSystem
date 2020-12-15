from django.shortcuts import render
from cmdb.models import Menu


# Create your views here.

def base_view(request):
    """
    顾客主界面
    """
    menu = Menu.objects.all()
    menu_None= menu is None
    return render(request,'C/base_view.html',{'menu':menu,'menu_None':menu_None})

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
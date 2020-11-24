from django.shortcuts import render

# Create your views here.


def base_view(request):
    """
    顾客主界面
    """
    return render(request,'C/base_view.html')

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
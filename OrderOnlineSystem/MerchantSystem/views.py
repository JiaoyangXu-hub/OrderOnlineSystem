from django.shortcuts import render

# Create your views here.

def base_view(request):
    """
    商家服务主界面
    """
    return render(request,'M/base_view.html')

def getCash_view(request):
    """
    提款成功界面
    """
    return render(request,'M/getCash_view.html')

def dealItem_view(request):
    """
    制作餐品
    """
    return render(request, "M/dealItem_view.html")

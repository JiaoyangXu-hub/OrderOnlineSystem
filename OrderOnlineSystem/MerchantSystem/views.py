from django.shortcuts import render,redirect,HttpResponse
from cmdb.models import Menu,Usr,Order
from Form import MerchantDish
# Create your views here.

def base_view(request):
    """
    商家服务主界面
    """
    if request.session['is_login']:
        menu = Menu.objects.all()
        user_id = request.session['user_id']
        return render(request,'M/base_view.html',{'menu':menu,'user_id':user_id})
    else:
        return redirect('/Login/')

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

def addDish(request):
    """
    添加餐品
    """
    addDishForm = MerchantDish()
    return render(request,"M/addDish_view.html",{'form':addDishForm})

def addDish_post(request):
    '''
    提交所添加表单后的反馈
    '''
    dish_form = MerchantDish(request.POST)
    if dish_form.is_valid() :
        dish = dish_form.clean()
        mid = Usr.objects.get(ID=request.session['user_id']) 
        Menu.objects.create(**dish,merchantID =mid)
        return redirect('/MerchantSystem/')
    elif dish_form.errors is not None:
        print(dish_form.errors)
        return HttpResponse(str(dish_form.errors))


def dishDetail(request,dishID):
    """
    展示餐品的评论以及维护餐品(修改或删除)
    """
    dish = Menu.objects.get(ID=dishID)
    dish_form = MerchantDish(data=dish.clean(),initial=dish.clean())
    d = dish_form.is_bound
    comment = Order.objects.filter(itemID=dishID).values('commentMerchant')
    return render(request,'M/detailDish.html',{'form':dish_form,'comment':comment,'dishID':dishID})


def delDish(request,dishID):
    """
    删除指定编号的餐品
    """
    Menu.objects.get(ID = dishID).delete()
    return redirect('/MerchantSystem/')

def updateDish_post(request,dishID):
    """
    接受修改菜品的请求
    """
    dish_form = MerchantDish(request.POST)
    if dish_form.is_valid() :
        dishChange = dish_form.clean()
        Menu.objects.filter(ID = dishID).update(**dishChange)
        return redirect('/MerchantSystem/')
    elif dish_form.errors is not None:
        print(dish_form.errors)
        return HttpResponse(str(dish_form.errors))
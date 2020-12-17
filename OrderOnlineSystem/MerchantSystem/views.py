from django.shortcuts import render,redirect,HttpResponse
from cmdb.models import Menu,Usr,Order,Bill,WaitCash
from Form import MerchantDish
from PIL import Image
# Create your views here.

def base_view(request):
    """
    商家服务主界面
    """
    if request.session['is_login']:
        # 选定商家
        user = Usr.objects.get(ID=request.session['user_id'])
        # 选定该商家的目录
        menu = Menu.objects.filter(merchantID=user)
        user_id = request.session['user_id']
        return render(request,'M/base_view.html',{'menu':menu,'user_id':user_id})
    else:
        return redirect('/Login/')


def dealItem_view(request):
    """
    查看历史订单,确认制作餐品
    """
    user = Usr.objects.get(ID=request.session['user_id'])
    # 该商家的订单,去掉待支付的项
    orders = Order.objects.filter(MerchantID=user).exclude(stage='待支付')
    return render(request, "M/dealItem_view.html",{'orders':orders,'user_id':request.session['user_id']})

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
    dish_form = MerchantDish()
    comment = Order.objects.filter(itemID=dish).values('commentMerchant')
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


def getCash_view(request):
    """
    点击提现按钮后，弹出提现提示页面
    """
    user = Usr.objects.get(ID=request.session['user_id'])
    bill = Bill.objects.filter(usrID=user)
    totalCount=0
    for item in bill:
        totalCount += item.price
    # 创建待提现表中的数据项
    WaitCash.objects.create(price=totalCount,usrID=user,note='等待提现')
    # 删除这些账单项
    Bill.objects.filter(usrID=user).delete()
    return render(request,'M/getCash_view.html',{'total':totalCount,'user_id':request.session['user_id']})


def dealItem_get(request,orderID):
    '''
    响应接单请求,并变换Order表的stage状态
    '''
    Order.objects.filter(orderID=orderID).update(stage='制作中')
    return redirect('/MerchantSystem/dealItem/')


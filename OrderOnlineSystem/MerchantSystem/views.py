from django.shortcuts import render,redirect,HttpResponse
from cmdb.models import Menu,Usr,Order,Bill,WaitCash
from Form import MerchantDish
from PIL import Image
import os
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
    查看订单信息,确认制作餐品
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
    if request.method == 'POST':
        dish_form = MerchantDish(request.POST,request.FILES)
        if dish_form.is_valid() :
            itemName = dish_form.cleaned_data['itemName']
            itemText = dish_form.cleaned_data['itemText']
            price = dish_form.cleaned_data['price']
            picture = dish_form.cleaned_data['picture']
            # dish = dish_form.clean()
            mid = Usr.objects.get(ID=request.session['user_id']) 
            # Menu.objects.create(**dish,merchantID =mid)
            dish = Menu(itemName=itemName,itemText=itemText,price=price,merchantID=mid,picture=picture)
            dish.save()
            return redirect('/MerchantSystem/')
        elif dish_form.errors is not None:
            print(dish_form.errors)
            return HttpResponse(str(dish_form.errors))
    else:
        dish_form = MerchantDish()
        return render(request,'M/addDish_view.html',{'form':dish_form})

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
    dish = Menu.objects.get(ID = dishID)
    pic_name = dish.picture.name
    # print(dish.picture.path)
    # print(pic_name)
    if dish.picture != '':
        path_abs = os.path.abspath('.') #取绝对路径
        os.remove(path_abs+'\\media\\'+pic_name) #删除服务器上存储的图片
    dish.delete() #删除表记录
    return redirect('/MerchantSystem/')

def updateDish_post(request,dishID):
    """
    接受修改菜品的请求
    """
    dish_form = MerchantDish(request.POST,request.FILES)
    if dish_form.is_valid() :
        dish = Menu.objects.get(ID = dishID)
        dish.itemName = dish_form.cleaned_data['itemName']
        dish.itemText = dish_form.cleaned_data['itemText']
        dish.price = dish_form.cleaned_data['price']
        dish.picture = dish_form.cleaned_data['picture']
        dish.save()
        # dishChange = dish_form.clean()        
        return redirect('/MerchantSystem/')
    elif dish_form.errors is not None:
        print(dish_form.errors)
        return HttpResponse(str(dish_form.errors))
    #  修改人：汤霖 提示用户做的尝试性修改，可以把原先的信息当作表格的placeholder属性显示出来
    # dish = Menu.objects.get(ID=dishID)
    # itemName = request.POST.get('itemName')
    # itemText = request.POST.get('itemText')
    # price = request.POST.get('price')
    # if itemName == '' and itemText == '' and price == '' :
    #     return render(request,'M/modifyDishError.html',{'dishID':dishID})
    # else:
    #     dish.itemName=itemName
    #     dish.itemText=itemText
    #     dish.price=price
    #     dish.save()
    #     return redirect('/MerchantSystem/')



def getCash_view(request):
    """
    点击提现按钮后，弹出提现提示页面
    """
    user = Usr.objects.get(ID=request.session['user_id'])
    bill = Bill.objects.filter(usrID=user)
    totalCount=0
    for item in bill:
        if  item.orderID.stage == '已完成' :
            totalCount += item.price
            item.delete()# 删除已完成的账单项
    # 创建待提现表中的数据项
    if totalCount != 0:
        WaitCash.objects.create(price=totalCount,usrID=user,note='商家等待提现')
    return render(request,'M/getCash_view.html',{'total':totalCount,'user_id':request.session['user_id']})


def dealItem_get(request,orderID):
    '''
    响应接单请求,并变换Order表的stage状态
    '''
    Order.objects.filter(orderID=orderID).update(stage='制作中')
    return redirect('/MerchantSystem/dealItem/')


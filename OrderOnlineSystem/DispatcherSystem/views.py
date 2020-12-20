from django.shortcuts import render,redirect,HttpResponse
from cmdb.models import Order,Bill,Usr,WaitCash

# Create your views here.

def base_view(request):
    """
    送餐员服务主界面
    """
    # 筛选出制作中和配送中的订单
    orders = Order.objects.filter(stage='制作中') | Order.objects.filter(stage='配送中')
    return render(request,'D/base_view.html',{'orders':orders,'user_id':request.session['user_id']})

def getCash_view(request):
    """
    提款成功界面
    """
    user = Usr.objects.get(ID=request.session['user_id'])
    bill = Bill.objects.filter(usrID=user)
    totalCount=0
    for item in bill:
        if item.orderID.stage == '已完成':
            totalCount += item.price
            item.delete()
    if totalCount != 0:
        WaitCash.objects.create(price=totalCount,usrID=user,note='配餐员等待提现')
    return render(request,'D/getCash_view.html',{'totalCount':totalCount,'user_id':request.session['user_id']})

def orderHistory_view(request):
    """
    查看历史接单
    """
    userId = request.session['user_id']
    user = Usr.objects.get(ID=userId)
    orders = Order.objects.filter(stage="已完成",DispatcherID=user)
    return render(request, "D/history_view.html",{'orders':orders,'user_id':request.session['user_id']})

def order_get(request,orderID):
    '''
    接收接单请求
    '''
    order = Order.objects.get(orderID=orderID)
    userId = request.session['user_id']
    user = Usr.objects.get(ID=userId)
    if order.stage == '制作中':
        Order.objects.filter(orderID=orderID).update(stage="配送中",DispatcherID=user)
        return redirect('/DispatcherSystem/')# 回到主界面,相当于刷新
    else:
        return HttpResponse('接单失败')
    
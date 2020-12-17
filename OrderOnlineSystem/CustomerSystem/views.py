from django.shortcuts import render,redirect,HttpResponse
from cmdb.models import Menu,Usr,Order,Bill
from Form import CommentForm
from OrderOnlineSystem.settings import BONUS# 在setting中更改配餐员每单利润

# Create your views here.

def base_view(request):
    """
    顾客主界面
    """
    if request.session['is_login']:
        menu = Menu.objects.all()
        return render(request,'C/base_view.html',{'menu':menu,'user_id':request.session['user_id'],'bonus':BONUS})
    else:
        return redirect('/Login/')

def order_view(request,dishID):
    """
    显示订单详情
    """
    orderData = Menu.objects.get(ID=dishID)
    return render(request,'C/order_view.html',{'orderData':orderData,'user_id':request.session['user_id'],'bonus':BONUS})


def pay_view(request,orderID):
    """
    缴费详情
    """
    oid = Order.objects.get(orderID = orderID)
    uid = request.session['user_id']
    price = oid.itemID.price + BONUS#加了小费
    bill = {'price':price,'user_id':uid,'order_id':orderID}
    return render(request,'C/pay_view.html',{'data':bill,'user_id':request.session['user_id']})


def order_submit(request,dishID):
    """
    提交订单，生成账单
    """
    itemID = Menu.objects.get(ID=dishID)
    mid = Usr.objects.get(ID=itemID.merchantID.ID)
    cid = Usr.objects.get(ID=request.session['user_id'])
    order = Order.objects.create(itemID=itemID,MerchantID=mid,CustomerID=cid,stage='待支付')
    return redirect('/CustomerSystem/pay/'+str(order.orderID))

def pay_submit(request,orderID):
    """
    缴费成功
    """
    Order.objects.filter(orderID=orderID).update(stage='已支付')
    order = Order.objects.get(orderID=orderID)
    # 给商家计入费用
    Bill.objects.create(orderID=order,price=order.itemID.price,usrID=order.MerchantID)
    # 给送餐员计入费用
    Bill.objects.create(orderID=order,price=BONUS,usrID=order.DispatcherID)
    return redirect('/CustomerSystem/')


def order_list_view(request):
    orders = Order.objects.filter(CustomerID=int(request.session['user_id']))
    return render(request,'C/order_list_view.html',{'orders':orders,'user_id':request.session['user_id']})

def order_confirm(request,orderID):
    """
    顾客确认订单收到
    """
    Order.objects.filter(orderID=orderID).update(stage='已完成')
    return redirect('/CustomerSystem/order/list/')

def comment(request,orderID):
    """
    顾客评论页面展示
    """
    order = Order.objects.get(orderID=orderID)
    commentForm = CommentForm()
    # 计算总价
    total = order.itemID.price+BONUS
    return render(request,'C/comment_view.html',{'form':commentForm,'order':order,'user_id':request.session['user_id'],'total':total})

def comment_post(request,orderID):
    """
    顾客评论
    """
    comments = CommentForm(request.POST)
    if comments.is_valid():
        tmp = comments.clean()
        Order.objects.filter(orderID=orderID,stage='已完成').update(**tmp)
        return redirect('/CustomerSystem/order/list/')
    else:
        return HttpResponse(str(comments.errors))




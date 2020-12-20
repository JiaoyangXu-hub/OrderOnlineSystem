from django.urls import path

from . import views

app_name = "CustomerSystem"

urlpatterns = [
    path('', views.base_view, name = "base"),# 顾客服务系统
    path('order/<int:dishID>/', views.order_view),# 订单详情
    path('order/<int:dishID>/submit/',views.order_submit),# 提交订单
    path('pay/<int:orderID>/', views.pay_view),# 缴费
    path('pay/<int:orderID>/submit/',views.pay_submit),#确认账单
    path('order/list/',views.order_list_view),#历史订单列表
    path('order/confirm/<int:orderID>/',views.order_confirm),#订单确认收到
    path('order/comment/<int:orderID>/',views.comment),#到达相应菜品的评论界面
    path('order/comment_post/<int:orderID>/',views.comment_post)#提交评论
]
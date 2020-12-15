from django.urls import path

from . import views

app_name = "CustomerSystem"

urlpatterns = [
    path('', views.base_view, name = "base"),# 顾客服务系统
    path('order', views.order_view, name = 'order'),# 订单详情
    path('pay', views.pay_view, name = 'pay')# 缴费
]
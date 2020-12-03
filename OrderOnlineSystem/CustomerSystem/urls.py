from django.urls import path

from . import views

app_name = "CustomerSystem"

urlpatterns = [
    path('', views.base_view),# 顾客服务系统
    path('', views.order_view),# 订单详情
    path('', views.pay_view)# 缴费
]
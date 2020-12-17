from django.urls import path

from . import views

app_name = "DispatcherSystem"

urlpatterns = [
    path('', views.base_view,name = 'base'),# 主界面
    path('getCash/',views.getCash_view),
    path('history/',views.orderHistory_view),# 查看历史接单页面
    path('order/<int:orderID>/',views.order_get),# 接单
]
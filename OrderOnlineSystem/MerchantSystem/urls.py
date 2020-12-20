from django.urls import path

from . import views

app_name = "MerchantSystem"

urlpatterns = [ 
    path('', views.base_view,name = 'base'),
    path('getCash/',views.getCash_view),
    path('dealItem/',views.dealItem_view),
    path('addDish/',views.addDish),             #添加菜品页面
    path('addDish_post/',views.addDish_post),   #添加菜品请求
    path('Dish/<int:dishID>/',views.dishDetail),# 维护菜品请求，返回一个维护网页
    path('Dish/<int:dishID>/updateDish_post/',views.updateDish_post),#修改菜品post表单提交
    path('DelDish/<int:dishID>/',views.delDish),# 删除菜品请求
    path('dealItem/<int:orderID>/',views.dealItem_get),# 处理接单请求

]


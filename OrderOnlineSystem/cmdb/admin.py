from django.contrib import admin
from .models import Usr,Order,Bill,WaitCash,Menu
# Register your models here.
from cmdb import models
# Register your models here.

def pay(modeladmin,request,queryest):
    queryest.update(是否转账=True)

pay.short_description = "进行转账"
    #可以统一对搜索出来的集合进行操作(比如是否付款)
    #这个操作可以出现让你点

@admin.register(Usr)
class UsrAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    actions_on_top = False
    fields = ('ID','location','phoneNumber','email','stage')
    #后台不能看到别人密码
    list_display = ('ID','location','phoneNumber','stage')
    #这里有一个bug是选择用户类型不会自动显示，要手动去点
    list_filter = ['stage']
    #可以进行分类选择
    search_fields = ['ID','location','phoneNumber','email']
    # actions = [pay]

@admin.register(WaitCash)
class WaitCashAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    actions_on_top = False
    list_display = ['ID','usrID','price','createTime','是否转账']
    actions = [pay]
    list_filter = ['是否转账']
    search_fields = ['usrID']
    ordering = ['ID']


# admin.site.register(models.Usr)
#把这个模型登记在后台
# admin.site.register(models.WaitCash)
# admin.site.register(models.Transfered)

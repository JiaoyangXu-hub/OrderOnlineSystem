from django.db import models

# Create your models here.

class Usr(models.Model):
    """
    用户数据库
    """
    _stage=[
        ('Customer','顾客'),
        ('Merchant','商家'),
        ('Dispacher','送餐员'),
    ]

    ID = models.CharField(primary_key=True,max_length=20,verbose_name="账号")
    password = models.CharField(null=False,max_length=20,verbose_name="密码")
    location = models.CharField(max_length=50,verbose_name="地址")
    phoneNumber = models.CharField(max_length=50,verbose_name="电话号码")
    email = models.EmailField(verbose_name="邮箱")
    stage = models.CharField(choices=_stage,max_length=20,verbose_name="身份")
    lastLoginTime = models.DateTimeField(auto_now_add=True,blank=False,editable=False,verbose_name="最后登录时间")

    class Meta:
        db_table = "Usr"
        verbose_name = "用户数据表"
        ordering = ['-lastLoginTime']
    pass

class Menu(models.Model):
    """
    餐品数据库
    """
    ID = models.IntegerField(primary_key=True,auto_created=True,editable=False)
    lastEditTime = models.DateTimeField(auto_now_add=True)
    merchantID = models.ForeignKey("Usr", verbose_name="商家账号", on_delete=models.CASCADE)
    itemName = models.CharField(max_length=20,verbose_name="餐品名")
    itemText = models.TextField(verbose_name="餐品简介")
    price = models.FloatField(verbose_name="餐品价格")
    class Meta:
        db_table = "Menu"
        verbose_name = "餐品数据表"
        ordering=['-lastEditTime']
    pass

class Order(models.Model):
    """
    订单数据库
    """
    _choice=[
        ('已下单','顾客已下单'),
        ('制作中','商家已接单'),
        ('配送中','配送员已接餐'),
        ('已完成','顾客已接餐')
    ]
    orderID = models.IntegerField(verbose_name="订单号")
    createTime = models.DateTimeField(auto_created=True, auto_now=True, auto_now_add=False,verbose_name="生成时间")
    CustomerID = models.ForeignKey("Usr", verbose_name="顾客ID", on_delete=models.CASCADE,related_name='CustomerID')
    MerchantID = models.ForeignKey("Usr", verbose_name="商家ID", on_delete=models.CASCADE,related_name='MerchantID')
    DispatcherID = models.ForeignKey("Usr", verbose_name="送餐员ID", on_delete=models.CASCADE,related_name='DispatcherID')
    itemID = models.ForeignKey("Menu",verbose_name='餐品号',on_delete=models.CASCADE)
    stage = models.CharField(choices=_choice,null=False,max_length=20,verbose_name='订单状态')
    commentMerchant = models.TextField(verbose_name="餐品评价")
    commentDispatcher = models.TextField(verbose_name="配送评价")
    class Meta:
        db_table = "Order"
        verbose_name = "订单数据表"
        ordering = ['-orderID']
    pass

class Bill(models.Model):
    """
    账单数据库
    """
    billID = models.IntegerField(primary_key=True,auto_created=True,editable=False)
    createTime = models.DateTimeField(auto_created=True, auto_now=True, auto_now_add=False,verbose_name="生成时间")
    usrID = models.ForeignKey("Usr", verbose_name='用户账号', on_delete=models.CASCADE)
    orderID = models.ForeignKey("Order", verbose_name="订单号", on_delete=models.CASCADE)
    price = models.FloatField(verbose_name="金额")
    class Meta:
        db_table = "Bill"
        verbose_name = "账单数据表"
        ordering=['-createTime']
    pass

class WaitCash(models.Model):
    """
    待提现数据库
    """
    ID = models.IntegerField(primary_key=True,auto_created=True,editable=False,verbose_name="单号")
    createTime = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name="生成时间")
    usrID = models.ForeignKey("Usr", verbose_name="用户ID", on_delete=models.CASCADE)
    price = models.FloatField(verbose_name="金额")
    note = models.TextField(verbose_name="备注")
    class Meta:
        db_table = "WaitCash"
        verbose_name = "待提现数据表"
        ordering=['-ID']
    pass

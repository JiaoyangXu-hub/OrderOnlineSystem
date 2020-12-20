from django import forms

class LoginForm(forms.Form):
    """
    登录表单
    """
    
    ID = forms.CharField(max_length=20,min_length=5,label='账号')
    password = forms.CharField(max_length=20,min_length=6,label='密码',widget=forms.PasswordInput)

class UsrForm(LoginForm):
    """
    用户注册表单，可将其参数传递到model.Usr 直接实例化，添加一条数据
    """
    _stage=[
        ('Customer','顾客'),
        ('Merchant','商家'),
        ('Dispatcher','送餐员'),
    ]
    phoneNumber = forms.RegexField(max_length=11,min_length=11,regex=r'1[3-9]\d{9}',label='Tel')
    email = forms.EmailField(label="邮箱",widget=forms.EmailInput)
    location = forms.CharField(label="地址")
    stage = forms.ChoiceField(choices=_stage,label="身份")

class MerchantDish(forms.Form):
    """
    商家菜品提交表单
    """
    itemName = forms.CharField(max_length=20,label="餐品名")
    itemText = forms.CharField(max_length=300,label="餐品简介")
    price = forms.FloatField(label="餐品价格")
    # picture = forms.ImageField(label='餐品图片')

class CommentForm(forms.Form):
    """
    顾客评论表单
    """
    commentMerchant = forms.CharField(max_length=200,label='菜品评价')
    commentDispatcher = forms.CharField(max_length=200,label='配送评价')



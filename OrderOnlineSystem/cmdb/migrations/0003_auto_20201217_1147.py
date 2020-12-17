# Generated by Django 3.1.3 on 2020-12-17 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0002_auto_20201216_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='picture',
            field=models.ImageField(null=True, upload_to='', verbose_name='餐品图片'),
        ),
        migrations.AlterField(
            model_name='order',
            name='stage',
            field=models.CharField(choices=[('待支付', '顾客已下单，未支付'), ('已支付', '顾客已下单，已支付'), ('制作中', '商家已接单'), ('配送中', '配送员已接餐'), ('已完成', '顾客已接餐'), ('已评价', '顾客已接餐')], max_length=20, verbose_name='订单状态'),
        ),
    ]
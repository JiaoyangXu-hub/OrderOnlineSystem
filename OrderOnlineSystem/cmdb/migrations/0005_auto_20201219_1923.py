# Generated by Django 2.1.5 on 2020-12-19 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0004_auto_20201217_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='picture',
            field=models.ImageField(default='img/default.jpg', null=True, upload_to='img/', verbose_name='餐品图片'),
        ),
    ]

# Generated by Django 3.1.13 on 2022-08-31 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(max_length=255, verbose_name='user appid')),
                ('appid', models.CharField(max_length=255, verbose_name='user appid')),
                ('shop_name', models.CharField(max_length=255, verbose_name='店铺名称')),
                ('shop_mode', models.CharField(max_length=255, verbose_name='店铺平台')),
                ('shop_appid', models.CharField(max_length=255, verbose_name='店铺appid')),
                ('shop_app_secret', models.CharField(max_length=255, verbose_name='店铺app secret')),
                ('shop_id', models.CharField(max_length=255, verbose_name='店铺id')),
                ('sandbox', models.IntegerField(default=1, verbose_name='沙箱')),
                ('proxy', models.IntegerField(default=0, verbose_name='是否代理ip')),
                ('proxy_ip', models.JSONField(default=dict, verbose_name='代理ip')),
                ('t_code', models.CharField(max_length=255, verbose_name='唯一值')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': 'DouYin Shop',
                'verbose_name_plural': 'DouYin Shop',
                'db_table': 'douyinshop',
                'ordering': ['id'],
            },
        ),
    ]

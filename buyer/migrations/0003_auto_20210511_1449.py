# Generated by Django 3.1.7 on 2021-05-11 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EcommerceProject', '0003_auto_20210211_1426'),
        ('buyer', '0002_address_order_orderproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='placed_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='EcommerceProject.userprofile'),
        ),
        migrations.AlterField(
            model_name='order',
            name='amt_status',
            field=models.CharField(default='unpaid', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='processing', max_length=40),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='status',
            field=models.CharField(default='processing', max_length=40),
        ),
    ]

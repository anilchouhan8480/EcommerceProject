# Generated by Django 3.1.7 on 2021-05-26 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buyer', '0004_auto_20210526_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='order_id',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='total_amt',
            field=models.DecimalField(decimal_places=3, max_digits=12),
        ),
    ]

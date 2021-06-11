# Generated by Django 3.1.7 on 2021-05-27 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0005_auto_20210526_1910'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='User',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='placed_by',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='product',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='OrderProduct',
        ),
    ]

# Generated by Django 2.1.7 on 2021-02-06 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_product_dated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Category',
            new_name='category',
        ),
    ]

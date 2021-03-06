# Generated by Django 3.1.7 on 2021-05-27 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('EcommerceProject', '0003_auto_20210211_1426'),
        ('seller', '0005_auto_20210527_0940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('desc', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('discounted_price', models.DecimalField(decimal_places=3, default=None, max_digits=10)),
                ('pro_img', models.ImageField(blank=True, upload_to='productimage')),
                ('qty', models.IntegerField()),
                ('description', models.TextField(default=None)),
                ('brand', models.CharField(default=None, max_length=100)),
                ('dated', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EcommerceProject.userprofile')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.category')),
            ],
        ),
    ]

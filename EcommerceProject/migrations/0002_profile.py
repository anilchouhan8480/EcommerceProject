# Generated by Django 2.1.7 on 2021-02-07 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EcommerceProject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_num', models.IntegerField()),
                ('pro_pic', models.ImageField(blank=True, null=True, upload_to='productimage')),
                ('age', models.CharField(blank=True, max_length=250)),
                ('address', models.CharField(blank=True, max_length=250)),
                ('gender', models.CharField(blank=True, max_length=250)),
                ('dateed', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='EcommerceProject.UserProfile')),
            ],
        ),
    ]
from django.db import models
from EcommerceProject.models import UserProfile
# Create your models here.

class Category(models.Model):
	catName = models.CharField(max_length=50)

class Product(models.Model):
	name = models.CharField(max_length=40)
	desc = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=10, decimal_places=3)
	pro_img = models.ImageField(upload_to="productimage", blank=True)
	qty = models.IntegerField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	added_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	dated = models.DateTimeField(auto_now=True)






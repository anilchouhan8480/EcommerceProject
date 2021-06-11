from django.db import models
from EcommerceProject.models import UserProfile

# Create your models here.

class Category(models.Model):
	catName = models.CharField(max_length=50)

class Product(models.Model):
	name = models.CharField(max_length=40)
	price = models.DecimalField(max_digits=10, decimal_places=3)
	discounted_price = models.DecimalField(max_digits=10, decimal_places=3, default=None)
	pro_img = models.ImageField(upload_to="productimage", blank=True)
	qty = models.IntegerField()
	description = models.TextField(default=None)
	brand = models.CharField(max_length=100, default=None)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	added_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	dated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.id)






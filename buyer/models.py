from django.db import models
from EcommerceProject.models import UserProfile
from seller.models import Product

# Create your models here.

class Cart(models.Model):
	class Meta():
		unique_together = ('product', 'user')
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	user = models.ForeignKey(UserProfile, on_delete= models.CASCADE)

class Order(models.Model):
	order_id = models.CharField(max_length=30)
	order_date = models.DateTimeField(auto_now=True)
	total_amt = models.DecimalField(decimal_places=3, max_digits=12)
	amt_status = models.CharField(max_length=20, default="unpaid")
	status = models.CharField(max_length=40, default="processing")
	placed_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None)

class OrderProduct(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	qty = models.IntegerField()
	status = models.CharField(max_length=40, default="processing")

class Address(models.Model):
	add_line1 = models.CharField(max_length=50)
	add_line2 = models.CharField(max_length=50)
	pincode = models.IntegerField()
	city = models.CharField(max_length=100)
	area = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)



			


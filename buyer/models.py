from django.db import models
from EcommerceProject.models import UserProfile
from django.contrib.auth.models import User
from seller.models import Product

# Create your models here.


STATE_CHOICES = (

	('Andhra Pradesh','Andhra Pradesh'),
	('Arunachal Pradesh ','Arunachal Pradesh '),
	('Assam','Assam'),
	('Bihar','Bihar'),
	('Chhattisgarh','Chhattisgarh'),
	('Goa','Goa'),
	('Gujarat','Gujarat'),
	('Haryana','Haryana'),
	('Himachal Pradesh','Himachal Pradesh'),
	('Jammu and Kashmir ','Jammu and Kashmir '),
	('Jharkhand','Jharkhand'),
	('Karnataka','Karnataka'),
	('Kerala','Kerala'),
	('Madhya Pradesh','Madhya Pradesh'),
	('Maharashtra','Maharashtra'),
	('Manipur','Manipur'),
	('Meghalaya','Meghalaya'),
	('Mizoram','Mizoram'),
	('Nagaland','Nagaland'),
	('Odisha','Odisha'),
	('Punjab','Punjab'),
	('Rajasthan','Rajasthan'),
	('Sikkim','Sikkim'),
	('Tamil Nadu','Tamil Nadu'),
	('Telangana','Telangana'),
	('Tripura','Tripura'),
	('Uttar Pradesh','Uttar Pradesh'),
	('Uttarakhand','Uttarakhand'),
	('West Bengal','West Bengal'),
	('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
	('Chandigarh','Chandigarh'),
	('Dadra and Nagar Haveli','Dadra and Nagar Haveli'),
	('Daman and Diu','Daman and Diu'),
	('Lakshadweep','Lakshadweep'),
	('National Capital Territory of Delhi','National Capital Territory of Delhi'),
	('Puducherry','Puducherry')

	)


class Cart(models.Model):
	class Meta():
		unique_together = ('product', 'user')
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	user = models.ForeignKey(UserProfile, on_delete= models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)

	def __str__(self):
		return str(self.id)

	@property
	def total_cost(self):
		return self.quantity * self.product.discounted_price
		


STATUS_CHOICES = (

	('Accepted','Accepted'),
	('Packed','Packed'),
	('On The Way','On The Way'),
	('Delivered','Delivered'),
	('Cancel','Cancel'),

	)

AMOUNT_STATUS_CHOICES = (

	('Paid','Paid'),
	('UnPaid','UnPaid')

	)




class Address(models.Model):
	add_line1 = models.CharField(max_length=50)
	add_line2 = models.CharField(max_length=50)
	pincode = models.IntegerField()
	city = models.CharField(max_length=100)
	area = models.CharField(max_length=100)
	state = models.CharField(choices=STATE_CHOICES, max_length=50)
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.id)


class OrderProduct(models.Model):
	customer = models.ForeignKey(Address, on_delete=models.CASCADE,default=None)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	order_id = models.CharField(max_length=30)
	order_date = models.DateTimeField(auto_now=True)
	total_amt = models.DecimalField(decimal_places=3, max_digits=12)
	qty = models.IntegerField(default=1)
	amt_status = models.CharField(max_length=20,choices=AMOUNT_STATUS_CHOICES, default="UnPaid")
	status = models.CharField(max_length=50,choices=STATUS_CHOICES, default="pending")
	placed_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None)


	def __str__(self):
		return str(self.id)

	@property
	def total_cost(self):
		return self.qty * self.product.discounted_price	
			


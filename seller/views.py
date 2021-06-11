from django.shortcuts import render, redirect
from EcommerceProject.models import UserProfile
from .models import Category, Product

# Create your views here.
def home(request):
	uObj = UserProfile.objects.get(user__username=request.user)
	return render(request, "WelcomeSeller.html", {'data' : uObj})

def add_product(request):
	catObjs = Category.objects.all()
	if request.method == "POST":
		pname = request.POST['pname']
		desc = request.POST['desc']
		price = request.POST['price']
		disc_price = request.POST['disc_price']
		brand = request.POST['brand']
		pImage = request.FILES['proimg']
		qty = request.POST['qty']
		catid = request.POST['cid']

		uObj = UserProfile.objects.get(user__username=request.user)
		catObj = Category.objects.get(id=catid)

		p = Product(name=pname, description=desc,discounted_price=disc_price,brand=brand, price=price, qty=qty, pro_img=pImage, category=catObj, added_by=uObj)
		p.save()
		return redirect('/seller/add_product/')
	return render(request, "AddProduct.html", {'catObjs' : catObjs})

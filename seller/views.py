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
		pImage = request.FILES['proimg']
		qty = request.POST['qty']
		catid = request.POST['cid']

		uObj = UserProfile.objects.get(user__username=request.user)
		catObj = Category.objects.get(id=catid)

		p = Product(name=pname, desc=desc, price=price, qty=qty, pro_img=pImage, category=catObj, added_by=uObj)
		p.save()
		return redirect('/seller/add_product/')
	return render(request, "AddProduct.html", {'catObjs' : catObjs})

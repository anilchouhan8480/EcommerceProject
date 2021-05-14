from django.shortcuts import render, redirect
from seller.models import Product, Category
from EcommerceProject.models import UserProfile
from django.shortcuts import render, redirect
from seller.models import Product, Category
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.hashers import check_password
import datetime
import random


# Create your views here.

def home(request):

    uObj = UserProfile.objects.get(user__username=request.user)
    cnt = Cart.objects.filter(user_id=uObj.id).count()

    cObjs = Category.objects.all()
    pObjs = Product.objects.all()
    return render(request, "WelcomeBuyer.html", {'cObjs':cObjs, 'pObjs':pObjs, 'count':cnt})

def add_cart(request, id):
    try:
        pObj = Product.objects.get(id=id)
        uObj = UserProfile.objects.get(user__username=request.user)

        c = Cart(product=pObj, user=uObj)
        c.save()
        return redirect('/buyer/home/')
    except:
        messages.error(request, "Aleady in your cart")
        return redirect('/buyer/home/')
	
def cartdetails(request):
	uObj = UserProfile.objects.get(user__username=request.user)
	cartObjs = Cart.objects.filter(user_id=uObj.id)
	#print(cartObjs)
	items = []

	for i in cartObjs:
		items.append(Product.objects.get(id=i.product_id))

	#print(items)
	return render(request, "CartDetails.html", {'pObjs':items})

def delcart(request, id):
	uObj = UserProfile.objects.get(user__username=request.user)
	pObj = Product.objects.get(id=id)

	c = Cart.objects.get(user=uObj, product=pObj)
	c.delete()
	return redirect('/buyer/cartdetails/')

def cartcalculate(request):
    uObj = UserProfile.objects.get(user__username=request.user)
    pQty = request.POST.getlist('p_qty')
    pid = request.POST.getlist('pid')
    price = request.POST.getlist('price')
    
    amount = 0

    for i in range(len(pQty)):
        amount = amount + (int(pQty[i])*float(price[i]))
        pObj = Product.objects.filter(id = pid[i])
        updatedQty = pObj[0].qty - int(pQty[i])
        pObj.update(qty = updatedQty)
        pro_obj = Product.objects.get(id = pid[i])

    c = Cart.objects.filter(user_id = uObj.id)
    c.delete()

    

    # Or(amount, pid, pQty, uObj)
    # send_mail("Order Update", "Order has been placed!", "gpmishra9@gmail.com",["anshika97mishra@gmail.com",])

    return render(request, "checkout.html")

		
def checkout(request):
	return render(request, "checkout.html")		



def profile(request):
    upObj = UserProfile.objects.filter(user__username=request.user)
    uObj = User.objects.filter(username = request.user)

    if request.method == "POST":
        a   = request.POST['subfirst']        
        b   = request.POST['last']
        c   = request.POST['email']
        d   = request.POST['mobile']

        upObj.update(mobile=d)
        uObj.update(first_name=a, last_name=b, email=c)

        return redirect('/buyer/profile/')

    return render(request, "profile.html", {'upObj' : upObj, 'uObj' : uObj,})

def catfilter(request, id):
	pObjs = Product.objects.filter(category_id=id)

	return render(request, "cartfilter.html", {'pObjs':pObjs})

	

def addcat(request):
	cname = request.POST['cat']
	catObj = Category(catName=cname)
	catObj.save()
	return redirect('/seller/add_product/')



def Or(amount, prod_id, prod_qty, uObj):

    tdate = str(datetime.date.today()).replace("-", "")
    rnum = random.randint(100,999)
    # s = []

    # for i in range(len(prod_id)): 
    #     s.append(str(prod_id[i]))

    l = ''.join(prod_id)

    or_id = tdate + "_" + l + "_" + str(rnum)

    O = Order(order_id=or_id, total_amt=amount, placed_by=uObj)
    O.save()

    for i in range(len(prod_id)):
        product_obj = Product.objects.get(id = prod_id[i])
        Op = OrderProduct(order=O, product= product_obj, qty=prod_qty[i])
        Op.save()




def myorder(request):

    uObj = UserProfile.objects.get(user__username=request.user)
    myOr = Order.objects.filter(placed_by = uObj.user_id)
    or_list = []
    or_dict = {}

    for i in range(len(myOr)):

        or_list.append(OrderProduct.objects.filter(order_id = myOr[i]))

        pl = []
        for j in range(len(or_list[i])):
            pl.append(Product.objects.filter(id = or_list[i][j].product_id))

        p2 = []

        for k in pl:
            p2.append(k[0])

        or_dict[myOr[i]] = p2

    return render(request, "myorder.html", {'or_dict': or_dict.items(), 'or_list' : or_list})	
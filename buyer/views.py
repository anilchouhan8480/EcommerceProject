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
from .forms import AddressForm
from django.db.models import Q
from django.http import JsonResponse
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

@login_required	
def cartdetails(request):
    uObj = UserProfile.objects.get(user__username=request.user)
    cartObjs = Cart.objects.filter(user_id=uObj.id)
    cnt = Cart.objects.filter(user_id=uObj.id).count()

    #print(cartObjs)
    items = []

    for i in cartObjs:
        items.append(Product.objects.get(id=i.product_id))

    # print(items)

    amount = 0.0
    shipping_amount = 70.0
    total_amt = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user==uObj] 
    print(cart_product)

    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += float(tempamount)
            totalamount = amount + shipping_amount

        return render(request, "CartDetails.html", {'pObjs':items,'totalamount':totalamount,'amount':amount,'count':cnt})

    else:
        return render(request, 'empty.html',{'count':cnt})


    return render(request, "CartDetails.html", {'pObjs':items, 'cartObjs':cartObjs,'count':cnt})

def product_detail(request, id):

    pObj = Product.objects.filter(id=id)


    return render(request, 'productdetail.html', {'pObj':pObj})

@login_required
def delcart(request, id):
    uObj = UserProfile.objects.get(user__username=request.user)
    pObj = Product.objects.get(id=id)

    c = Cart.objects.get(user=uObj, product=pObj)
    c.delete()
    return redirect('/buyer/cartdetails/')


def plus_cart(request):
    uObj = UserProfile.objects.get(user__username=request.user)
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=uObj))
        c.quantity+=1
        c.save()
        cart_product = [p for p in Cart.objects.all() if p.user==uObj] 

        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += float(tempamount)
            totalamount = amount + shipping_amount

        data = {

            'quantity' : c.quantity,
            'amount' : amount,
            'totalamount' : totalamount
        }

        return JsonResponse(data)



def minus_cart(request):
    uObj = UserProfile.objects.get(user__username=request.user)
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=uObj))
        c.quantity+=1
        c.save()
        cart_product = [p for p in Cart.objects.all() if p.user==uObj] 

        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount -= float(tempamount)
            totalamount = amount + shipping_amount

        data = {

            'quantity' : c.quantity,
            'amount' : amount,
            'totalamount' : totalamount
        }

        return JsonResponse(data)




def cartcalculate(request):
    # uObj = UserProfile.objects.get(user__username=request.user)
    # pQty = request.POST.getlist('p_qty')
    # pid = request.POST.getlist('pid')
    # price = request.POST.getlist('price')
    
    # amount = 0

    # for i in range(len(pQty)):
    #     amount = amount + (int(pQty[i])*float(price[i]))
    #     pObj = Product.objects.filter(id = pid[i])
    #     updatedQty = pObj[0].qty - int(pQty[i])
    #     pObj.update(qty = updatedQty)
    #     pro_obj = Product.objects.get(id = pid[i])

    # c = Cart.objects.filter(user_id = uObj.id)
    # c.delete()

    

    # Or(amount, pid, pQty, uObj)
    # send_mail("Order Update", "Order has been placed!", "gpmishra9@gmail.com",["anshika97mishra@gmail.com",])


    return render(request, "checkout.html")

@login_required
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

    return render(request, "profile.html", {'upObj' : upObj, 'uObj' : uObj, 'active':'btn-primary'})

@login_required
def address(request):
    uObj = UserProfile.objects.get(user__username=request.user)
    cnt = Cart.objects.filter(user_id=uObj.id).count()
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            # uObj = UserProfile.objects.filter(user__username=request.user)
            l1 = form.cleaned_data['add_line1']
            l2 = form.cleaned_data['add_line2']
            p = form.cleaned_data['pincode']
            c = form.cleaned_data['city']
            a = form.cleaned_data['area']
            s = form.cleaned_data['state']


            add = Address(add_line1=l1,add_line2=l2,pincode=p,city=c,area=a,state=s, user=uObj)
            add.save()
            messages.success(request, 'Congratulations!! Address Added successFully')
            return redirect('/buyer/address/')
        return render(request, "address.html",{'form':form,'active':'btn-primary','count':cnt})   


    else:
        form = AddressForm()

        uAobj = Address.objects.filter(user_id=uObj.id)

        return render(request, "address.html",{'uAobj':uAobj, 'form':form, 'active':'btn-primary','count':cnt}) 

    return render(request, "address.html",{'uAobj':uAobj,'active':'btn-primary','count':cnt})

def catfilter(request, id):
	pObjs = Product.objects.filter(category_id=id)

	return render(request, "cartfilter.html", {'pObjs':pObjs})

	

def addcat(request):
	cname = request.POST['cat']
	catObj = Category(catName=cname)
	catObj.save()
	return redirect('/seller/add_product/')

@login_required
def checkout(request):
    uObj = UserProfile.objects.get(user__username=request.user)

    add = Address.objects.filter(user=uObj)

    cartObj = Cart.objects.filter(user=uObj)

    amount = 0.0
    shipping_amount = 70.0
    total_amt = 0.0

    cart_product = [p for p in Cart.objects.all() if p.user==uObj] 

    if cart_product:

        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += float(tempamount)
        totalamount = amount + shipping_amount



    return render(request, "checkout.html",{'add':add, 'totalamount':totalamount,'cartObj':cartObj})

@login_required
def payment_done(request):
    uObj = UserProfile.objects.get(user__username=request.user)
    user = User.objects.filter(id=uObj.id)
    custid = request.GET.get('custid')
    customer = Address.objects.get(id=custid)
    cart = Cart.objects.filter(user=uObj)

    amount = 0.0
    shipping_amount = 70.0
    total_amt = 0.0

    cart_product = [p for p in Cart.objects.all() if p.user==uObj] 

    if cart_product:

        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += float(tempamount)
        totalamount = amount + shipping_amount


    tdate = str(datetime.date.today()).replace("-", "")
    rnum = random.randint(100,999)
    l = ''.join(custid)

    or_id = tdate + "_" + l + "_" + str(rnum)
    for c in cart:
        O = OrderProduct(order_id=or_id,order_date=tdate,total_amt=totalamount,customer=customer, qty=c.quantity, placed_by=uObj,product=c.product)
        O.save()
        c.delete()
    return redirect('/buyer/orders/')     


def Or(amount, prod_id, prod_qty, uObj):

    pass

    # tdate = str(datetime.date.today()).replace("-", "")
    # rnum = random.randint(100,999)
    # # s = []

    # # for i in range(len(prod_id)): 
    # #     s.append(str(prod_id[i]))

    # l = ''.join(prod_id)

    # or_id = tdate + "_" + l + "_" + str(rnum)

    # O = Order(order_id=or_id, total_amt=amount, placed_by=uObj)
    # O.save()

    # for i in range(len(prod_id)):
    #     product_obj = Product.objects.get(id = prod_id[i])
    #     Op = OrderProduct(order=O, product= product_obj, qty=prod_qty[i])
    #     Op.save()


@login_required
def myorders(request):

    uObj = UserProfile.objects.get(user__username=request.user)
    op = OrderProduct.objects.filter(placed_by=uObj)

    return render(request, "myorder.html", {'orders':op})
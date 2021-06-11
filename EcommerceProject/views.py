from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import UserProfile
from seller.models import *
from buyer.models import *
from .forms import MyPasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail

import random

def home(request):

	cObjs = Category.objects.all()
	pObjs = Product.objects.all()

	return render(request, "index.html",{'cObjs':cObjs, 'pObjs':pObjs,})



def signup(request):
	if request.method == "POST":
		un = request.POST['uname']
		pwd = request.POST['pwd']
		fn = request.POST['fname']
		ln = request.POST['lname']
		email = request.POST['email']
		mob = request.POST['mob']
		role = request.POST['role']

		u = User(username=un,password=make_password(pwd),first_name=fn,last_name=ln,email=email)
		u.save()

		up = UserProfile(user=u, mobile=mob,role=role)
		up.save()
		messages.success(request, "Congrats! Your have Successfully Created your Account,Now Login For Great Exprience.")
		return redirect('/login/')

	return render(request, "signup.html")

def login_call(request):
	if request.method == "POST":
		un = request.POST['uname']
		pwd = request.POST['pwd']

		user = authenticate(username=un, password=pwd)

		if user:
			login(request, user)
			uObj = UserProfile.objects.get(user__username=request.user)
			
			if uObj.role == "Seller":
				messages.success(request,'Login Suucess! Welcome. ')
				return redirect('/seller/home/')

			elif uObj.role == "Buyer":
				messages.success(request,'Login Suucess! Welcome. ')
				return redirect('/buyer/home/')
			
			return render(request, 'index.html')
		else:
			messages.error(request,'username or password not correct')
			return redirect('/login/')


	return render(request, "login.html")


# def forgot(request):

#     code = random.randint(1000, 9999)
#     send_mail("Reset Link", str(code), "anilchouhan8480@gmail.com",["chauhananil152@gmail.com",])

#     if request.method == "POST":
#         v = request.POST['code']

#         if code == v:
#             paswd = request.POST['password']
#             uObj = UserProfile.objects.get(user__username=request.user)
#             u = User.objects.get(id = uObj.user_id)
#             u.update(password = paswd)
#             u.save()
#         else:
#             return redirect('/forgotpassword/')


    # return render(request, "reset_password.html")

def reset_password(request):
    if request.method == "POST":
        j = request.POST['password']

        u = User(password=make_password(j))
        u.update()
        return redirect('/login/')
    return render(request, "reset_password.html")
	

def logout_call(request):
	logout(request)
	return redirect('/login/')
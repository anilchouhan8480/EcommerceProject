from django.urls import path
from . import views

app_name = 'buyer'

urlpatterns = [
	path('home/', views.home),
	path('add_cart/<int:id>/', views.add_cart, name='add_cart'),
	path('cartdetails/', views.cartdetails, name='cartdetails'),
	path('delcart/<int:id>/', views.delcart, name="delcart"),
	path('cartcalculate/', views.cartcalculate),
	path('checkout/', views.checkout),
	path('paymentdone/', views.payment_done, name='paymentdone'),
	path('profile/', views.profile, name="profile"),
	path('address/', views.address, name="address"),
	path('catfilter/<int:id>/', views.catfilter, name="catfilter"),
	path('addcat/', views.addcat),
	path('pluscart/', views.plus_cart, name='pluscart'),
	path('minuscart/', views.minus_cart, name='minuscart'),
	path('orders/', views.myorders, name="orders"),
    path('product-detail/<int:id>/', views.product_detail, name='product-detail'),
]
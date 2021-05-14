from django.urls import path
from . import views

app_name = 'buyer'

urlpatterns = [
	path('home/', views.home),
	path('add_cart/<int:id>/', views.add_cart, name='add_cart'),
	path('cartdetails/', views.cartdetails),
	path('delcart/<int:id>/', views.delcart, name="delcart"),
	path('cartcalculate/', views.cartcalculate),
	path('checkout/', views.checkout),
	path('profile/', views.profile, name="profile"),
	path('catfilter/<int:id>/', views.catfilter, name="catfilter"),
	path('addcat/', views.addcat),
	path('myorder/', views.myorder)

]
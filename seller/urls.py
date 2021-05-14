from django.urls import path
from . import views

urlpatterns = [
	path('home/', views.home),
	path('add_product/',views.add_product)
]
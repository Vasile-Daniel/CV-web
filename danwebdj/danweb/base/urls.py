# no. 3 acest fisier url.py a fost ceat de mine de la zero 
from django.urls import path
# din foldarul 
from . import views

urlpatterns = [
	path('', views.home)
]

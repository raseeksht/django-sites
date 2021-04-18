from django.shortcuts import render

from .models import Laptop
# Create your views here.

def index(request):
	laps = Laptop.objects.all()
	values = {"laptops":laps}
	return render(request,'index.html',values)

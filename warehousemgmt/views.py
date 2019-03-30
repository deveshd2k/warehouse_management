from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def home(request):
	return render(request,'home.html')

def warehouse_signup(request):
	return render(request,'warehouse_signup.html')

def shop_signup(request):
	return render(request,'shop_signup.html')

def login(request):
	return render(request,'login.html')

def dashboard(request):
	return render(request,'warehouse_dashboard.html')
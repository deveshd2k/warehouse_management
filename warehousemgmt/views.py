from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from .forms import WarehouseSignUpForm, ShopkeeperSignUpForm, SearchForm
from .models import Manager,Shopkeeper,Product
from .resources import ProductResource
from tablib import Dataset
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
	return render(request,'home.html')

def warehouse_signup(request):
	if request.method == "POST":
		form = WarehouseSignUpForm(request.POST)
		if form.is_valid():	
			addManager = Manager()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			addManager.username = form.cleaned_data['username']
			addManager.name = form.cleaned_data['name']
			addManager.warehouse_name = form.cleaned_data['warehouse_name']
			addManager.location = form.cleaned_data['location']
			addManager.capacity = form.cleaned_data['capacity']
			addManager.contact = form.cleaned_data['contact']
			addManager.save()
			form.save()
			user = authenticate(username=username, password=raw_password)
			login(request,user)
			return HttpResponseRedirect('warehouse_dashboard')
		else:
			print(form.errors)
	else:
		form = WarehouseSignUpForm()
	return render(request,'warehouse_signup.html',{'form':form})

def shop_signup(request):
	if request.method == "POST":
		form = ShopkeeperSignUpForm(request.POST)
		if form.is_valid():	
			addShopkeeper = Shopkeeper()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			addShopkeeper.username = form.cleaned_data['username']
			addShopkeeper.name = form.cleaned_data['name']
			addShopkeeper.shop_name = form.cleaned_data['shop_name']
			addShopkeeper.location = form.cleaned_data['location']
			addShopkeeper.contact = form.cleaned_data['contact']
			addShopkeeper.save()
			form.save()
			user = authenticate(username=username, password=raw_password)
			login(request,user)
			return HttpResponseRedirect('shop_dashboard')
		else:
			print(form.errors)
	else:
		form = WarehouseSignUpForm()
	return render(request,'shop_signup.html',{'form':form})

@login_required(login_url='login')
@csrf_exempt
def user_login(request):
	if request.user.is_staff:
		return redirect('warehouse_dashboard')
	else:
		return redirect('shop_dashboard')

@login_required(login_url='login')
@csrf_exempt
def warehouse_dashboard(request):
	total = Product.objects.aggregate(Sum('quantity'))['quantity__sum']
	if total == None:
		total=0
	username = request.user.username
	print(total)
	total_quantity = Manager.objects.filter(username=username).values('capacity')[0]['capacity']
	percent = ((total_quantity-total)/total_quantity)*100
	queryset = Manager.objects.filter(username=username)
	instance = Product.objects.all()
	if request.method == 'POST' and request.FILES['myfile']:
		product_resource = ProductResource()
		dataset = Dataset()
		new_product = request.FILES['myfile']

		imported_data = dataset.load(new_product.read().decode('utf-8'),format='csv')
		result = product_resource.import_data(dataset, dry_run = True)

		if not result.has_errors():
			product_resource.import_data(dataset, dry_run=False)
	return render(request,'warehouse_dashboard.html',{'queryset':queryset,'instance':instance,'percent':percent})

@login_required(login_url='login')
@csrf_exempt
def shop_dashboard(request):
	username = request.user.username
	queryset = Shopkeeper.objects.filter(username=username)
	instance = None
	if request.method == "POST":
		form = SearchForm(request.POST)
		if form.is_valid():
			p_id = form.cleaned_data['p_id']
			instance = Product.objects.filter(p_id=p_id)
		else:
			print(form.errors)
	else:
		form = SearchForm()
	return render(request,'shop_dashboard.html',{'queryset':queryset,'instance':instance})

def userlogout(request):
	logout(request)
	return HttpResponseRedirect('/')

def barcode(request):
	return render(request,'barcode.html')
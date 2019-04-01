from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class WarehouseSignUpForm(UserCreationForm):
	name = forms.CharField(max_length=30)
	username = forms.CharField(max_length=20)
	warehouse_name = forms.CharField(max_length=60)
	location = forms.CharField(max_length=100)
	capacity = forms.CharField(max_length=10)
	contact = forms.CharField(max_length=14)

	class Meta:
		model = User
		fields = ('name','username','password1','password2','warehouse_name','location','capacity','contact' )

		def clean_username(self):
			username = self.cleaned_data['username'].lower()
			r = User.objects.filter(username=username)
			if r.count():
				raise  ValidationError("Username already exists")
			return username

		def clean_password2(self):
			password1 = self.cleaned_data.get('password1')
			password2 = self.cleaned_data.get('password2')
			if password1 and password2 and password1 != password2:
				raise ValidationError("Passwords don't match")
				return password2

	def save(self, commit=True):
		user = super (WarehouseSignUpForm , self ).save(commit=False)
		user.is_staff = True

		if commit:
			user.save()
		return user

class ShopkeeperSignUpForm(UserCreationForm):
	name = forms.CharField(max_length=30)
	username = forms.CharField(max_length=20)
	shop_name = forms.CharField(max_length=60)
	location = forms.CharField(max_length=100)
	contact = forms.CharField(max_length=14)

class Meta:
	model = User
	fields = ('name','username','password1','password2','shop_name','location','contact' )

	def clean_username(self):
		username = self.cleaned_data['username'].lower()
		r = User.objects.filter(username=username)
		if r.count():
			raise  ValidationError("Username already exists")
		return username

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise ValidationError("Passwords don't match")
			return password2

class SearchForm(forms.Form):
	p_id = forms.CharField(max_length=20)
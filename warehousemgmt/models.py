from django.db import models

class Manager(models.Model):
	name = models.CharField(max_length=30)
	username = models.CharField(max_length=20)
	warehouse_name = models.CharField(max_length=60)
	location = models.CharField(max_length=100)
	capacity = models.IntegerField()
	contact = models.CharField(max_length=14)

	def __str__(self):
		return self.username

class Shopkeeper(models.Model):
	name = models.CharField(max_length=30)
	username = models.CharField(max_length=20)
	shop_name = models.CharField(max_length=60)
	location = models.CharField(max_length=100)
	contact = models.CharField(max_length=14)

	def __str__(self):
		return self.username

class Product(models.Model):
	p_id = models.CharField(max_length=10)
	name = models.CharField(max_length=20)
	quantity = models.IntegerField()
	prop1 = models.CharField(max_length=30)
	prop2 = models.CharField(max_length=30)

	def __str__(self):
		return self.p_id
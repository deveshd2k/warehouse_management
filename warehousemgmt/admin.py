from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Manager,Shopkeeper,Product
# Register your models here.
admin.site.register(Manager)
admin.site.register(Shopkeeper)

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    pass
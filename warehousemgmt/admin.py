from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Manager,Shopkeeper,Product,Photographer,ProductImage
# Register your models here.
admin.site.register(Manager)
admin.site.register(Shopkeeper)
admin.site.register(Photographer)
admin.site.register(ProductImage)

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    pass
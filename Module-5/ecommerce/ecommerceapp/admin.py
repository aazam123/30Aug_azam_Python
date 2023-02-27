from django.contrib import admin
from .models import Product
# Register your models here.

class signupModel(admin.ModelAdmin):
    ordering=['id']
    list_display=['product_id','product_name','product_dicription']

admin.site.register(Product)
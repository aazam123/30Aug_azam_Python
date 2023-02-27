from django.contrib import admin
from .models import studinfo
# Register your models here.

class signupModel(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','firstname','lastname','mobile','email','password','repeatepassword','address','city','state']

admin.site.register(studinfo,signupModel)

from django.shortcuts import render, redirect
from .models import studinfo
from .form import user_form
# Create your views here.

def index(request):
    if request.method=='POST':
        user=user_form(request.POST)
        if user.is_valid():
            user.save()
            print("your acount crt")
        else:
            print(user.errors)
    else:
        data=studinfo()
    return render(request,'index.html')

def show(request): 
    data={'stdata':studinfo.objects.all}
    return render(request,'show.html',{'data':data,'stdata':studinfo.objects.all})

def update(request,id):
    data=studinfo.objects.get(id=id)
    if request.method=='POST':
        stupdate=user_form(request.POST)
        if stupdate.is_valid():
            stupdate=user_form(request.POST,instance=data)
            stupdate.save()
            print("Record updated!")
            return redirect("show")
        else:
            print(stupdate.errors)
    return render(request,'update.html',{'id':studinfo.objects.get(id=id)})

def delete(request,id):
    data=studinfo.objects.get(id=id)
    studinfo.delete(data)
    return redirect('show')


from django.contrib import admin
from django.urls import path
from insertapp import views

urlpatterns = [
   path('admin/',admin.site.urls),
   path('',views.index),
   path('oderadd/',views.oderadd),
   path('addproduct/',views.addproducts),

#    path('contact/',views.contact),
]
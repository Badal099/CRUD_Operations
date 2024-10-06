from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('addemployee/', views.AddEmployee, name='addemployee'),
    path('delete/<id>', views.DeleteData, name='deletedata'),
    path('update/<id>', views.UpdateData, name='updatedata'),
]

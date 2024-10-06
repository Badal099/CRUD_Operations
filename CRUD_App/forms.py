from django import forms
from .models import Employee

class employeeDetails(forms.Form):
    empid = forms.CharField(label='Employee ID', widget=forms.TextInput(attrs={'class':'form-control'}))
    empname = forms.CharField(label='Employee Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    empdesignation = forms.CharField(label='Designation', widget=forms.TextInput(attrs={'class':'form-control'}))
    empcontact = forms.IntegerField(label='Contact Number', widget=forms.TextInput(attrs={'class':'form-control'}))
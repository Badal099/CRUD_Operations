from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Employee
from .forms import employeeDetails

# Create your views here.
def HomePage(request):
    data  = Employee.objects.all()
    return render(request, 'home.html', {'data':data})

def AddEmployee(request):
    if request.method == "POST":
        detail = employeeDetails(request.POST)
        if detail.is_valid():
            empid = detail.cleaned_data['empid']
            empname = detail.cleaned_data['empname']
            empdesignation = detail.cleaned_data['empdesignation']
            empcontact = detail.cleaned_data['empcontact']
            emp_detail = Employee(empid=empid, empname=empname, empdesignation=empdesignation, empcontact=empcontact)
            emp_detail.save()
            return HttpResponseRedirect('/')
    else:
        detail = employeeDetails()
    return render(request, 'addemployee.html', {'detail':detail})

def DeleteData(request, id):
    data  = Employee.objects.get(pk=id)
    data.delete()
    return HttpResponseRedirect('/')

def UpdateData(request, id):
    data  = Employee.objects.get(pk=id)
    if request.method == "POST":
        empid = request.POST['empid']
        empname = request.POST['empname']
        empdesignation = request.POST['empdesignation']
        empcontact = request.POST['empcontact']
        data.empid = empid
        data.empname = empname
        data.empdesignation = empdesignation
        data.empcontact = empcontact
        data.save()
        return HttpResponseRedirect('/')
    return render(request, 'updatedata.html', {'data': data})
    





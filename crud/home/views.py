from django.shortcuts import render,redirect
from .models import Person
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages

def from_data(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        Company_name=request.POST['company']
        Email_name=request.POST['Email']
        Phone_number=request.POST['Phone']
        Password=make_password(request.POST['Password'])
        if Person.objects.filter(Phone_number=Phone_number).exists():
            messages.error(request,"phone number already exists")
            return redirect('/')

        elif Person.objects.filter(Email_name=Email_name).exists():
            messages.error(request,"phone number already exists")
            return redirect('/')
        else :
             Person.objects.create().exists(first_name=first_name,last_name=last_name,Company_name=Company_name,
             Email_name=Email_name,Phone_number=Phone_number,Password=Password)

def welcome(request):
    return render(request,"temp/welcome.html")
def home(request):
    return render(request,"temp/home.html")
def login(request):
    return render(request,"temp/login.html")
def table(request):
    return render(request,"temp/table.html")
def update(request):
    return render(request,"temp/update.html")
def base(request):
    return render(request,"temp/base.html")
    
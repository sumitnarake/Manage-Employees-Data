from pyexpat.errors import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from employee.models import employeenames


def register(request):
    try:
        if request.method =="POST":
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password1')
            en=User(username=username, email=email,password=password)
            en.save()
            return redirect('login')
    except:
        pass
    return render(request,"register.html")

def login(request):
    try:
        if request.method =="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            p=auth.authenticate(username=username,password=password)
            if p is not None:
                auth.login(request,p)
                return redirect('home')
            else:
                messages.error(request,"invalid creadital")
                return redirect('login')
        else:
            return render(request, "login.html")
    except:
        pass
    return render(request,"login.html")
    # return HttpResponse("hii this is sumit narake")

def home(request):
    emp=employeenames.objects.all()
    context={
        'emp':emp
    }
    return render(request,"home.html",context)

def add(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        emp=employeenames( name= name,email=email,address=address,phone=phone)
        emp.save()
        return redirect('home')
    return render(request,'home.html')

def edit(request):
    emp=employeenames.objects.all()
    context={
        'emp':emp
    }
    return redirect(request,"home.html",context)

def update(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        emp=employeenames( id=id,name= name,email=email,address=address,phone=phone)
        emp.save()
        return redirect('home')
    return redirect(request,'home.html')

def delete(request,id):
    emp=employeenames.objects.filter(id=id)
    emp.delete()
    context={
        'emp':emp
    }
    return redirect('home')

def logout(request):
    auth.logout(request)
    return redirect(request,"login.html")
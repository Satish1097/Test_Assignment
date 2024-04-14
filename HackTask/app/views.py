from django.shortcuts import render,redirect
from .models import User,Task


# Create your views here.
def home(request):
    return render(request,"index.html")
def Add_User(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        data=User(name=name,email=email,mobile=mobile)
        data.save()
        return render(request,'UserList.html')

    return render(request,'Adduser.html')

def UserList(request):
    return render(request,"UserList.html")

def Add_Task(request):
    if request.method=="GET":
        return render(request,'addtask.html')

def TaskList(request):
    return render(request,'TaskList.html')
from django.shortcuts import render
from .forms import *

# Create your views here.
def home(request):
    Context={}
    Context['form'] = StudentForm
    return render(request,'home.html',Context)

def register(request):
    print(request)
    name = request.POST.get('Name')
    email = request.POST.get('Email')
    contact = request.POST.get('Contact')
    data = Student.objects.filter(Email = email)
    if (data):
        msg="Email already Exist"
        return render(request,"home.html",{'key':msg})
    else:
        Student.objects.create(Name=name,Email=email,Contact=contact)
        msg="Registration Successfully"
        return render(request,'home.html',{'key':msg})


from django.shortcuts import render,redirect
from .forms import UserCreationForm,loginUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.
def login_user(request):
    form = loginUserForm()
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')
        user = authenticate(request,email=email,password=password,role=role)
        if user:
            login(request,user)
            messages.success(request, "You have successfully logged in.")
            return redirect('Student')
        else:
            messages.error(request, "Invalid email or password.")
    return render(request,'login.html',{
        'form':form
    })

def Signup_user(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User registered successfully")
            return redirect('login')
    return render(request,'Signup.html',{
        'form':form
    })


def student(request):
    return render(request,'Student/Student.html')
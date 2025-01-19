from django.shortcuts import render,redirect
from .forms import UserCreationForm,loginUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
# Authenticate a user and log into the dashboard
def login_user(request):
    form = loginUserForm()
    if request.method == "POST":
        form = loginUserForm(request,data=request.POST) 
        # role = request.POST.get('role')
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            role = request.POST['role']
            user = authenticate(request,username=username,password=password,role=role)
            if user is not None:
                login(request,user)
                messages.success(request, "You have successfully logged in.")
                return redirect('Student')
        else:
            messages.error(request, "Invalid email or password.")
    return render(request,'login.html',{
        'form':form
    })



# Register a user
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



# Student Dashboard
def student(request):
    return render(request,'Student/Student.html')
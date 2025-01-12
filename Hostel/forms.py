from django import forms
from .models import UserModel,UserType
from django.forms import widgets

# User login and Signup form
class UserCreationForm(forms.ModelForm):
    first_name = forms.CharField(required=True,widget=widgets.TextInput(attrs={'placeholder':'Abc', 'class':'form-control'}),label="Enter your first Name")
    last_name = forms.CharField(required=True,widget=widgets.TextInput(attrs={'placeholder':'Abc', 'class':'form-control'}),label="Enter your last Name")
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder':'Abc@gmail.com', 'class':'form-control'}),label="Enter your email")
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': '********', 'class': 'form-control'}),
        label="Enter password"
    )
    role = forms.ModelChoiceField(
        queryset=UserType.objects.all(),
        widget=forms.Select(attrs={'class':'form-control'}),
        label="Selet a role"
    )
    class Meta:
        model = UserModel
        fields = ['first_name','last_name','email','password','role']


class loginUserForm(forms.ModelForm):
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder':'Abc@gmail.com', 'class':'form-control'}),label="Enter your email")
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': '********', 'class': 'form-control'}),
        label="Enter password"
    )
    role = forms.ModelChoiceField(
        queryset=UserType.objects.all(),
        widget=forms.Select(attrs={'class':'form-control'}),
        label="Selet a role"
    )
    class Meta:
        model = UserModel
        fields = ['email','password','role']

from django import forms
from django.forms import widgets
from .models import UserType
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm


# User login and Signup form
class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder':'Abc@gmail.com', 'class':'form-control'}),label="Enter your email")
    class Meta:
        model = User
        fields = ['username','email','password1']


class loginUserForm(AuthenticationForm):
   
    class Meta:
        model = User
        fields = ['email','password']



# email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder':'Abc@gmail.com', 'class':'form-control'}),label="Enter your email")
#     password = forms.CharField(
#         required=True,
#         widget=forms.PasswordInput(attrs={'placeholder': '********', 'class': 'form-control'}),
#         label="Enter password"
#     )
#     role = forms.ModelChoiceField(
#         queryset=UserType.objects.all(),
#         widget=forms.Select(attrs={'class':'form-control'}),
#         label="Selet a role"
#     )



#   first_name = forms.CharField(required=True,widget=widgets.TextInput(attrs={'placeholder':'Abc', 'class':'form-control'}),label="Enter your first Name")
#     last_name = forms.CharField(required=True,widget=widgets.TextInput(attrs={'placeholder':'Abc', 'class':'form-control'}),label="Enter your last Name")
#     email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder':'Abc@gmail.com', 'class':'form-control'}),label="Enter your email")
#     password = forms.CharField(
#         required=True,
#         widget=forms.PasswordInput(attrs={'placeholder': '********', 'class': 'form-control'}),
#         label="Enter password"
#     )
#     role = forms.ModelChoiceField(
#         queryset=UserType.objects.all(),
#         widget=forms.Select(attrs={'class':'form-control'}),
#         label="Selet a role"
#     )
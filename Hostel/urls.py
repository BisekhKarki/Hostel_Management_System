from django.urls import path,include
from . import views

urlpatterns = [
    path('login/',views.login_user,name='login'),
    path('Signup/',views.Signup_user,name='Signup'),
    path('',views.student,name='Student')
]
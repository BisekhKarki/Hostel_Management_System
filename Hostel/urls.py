from django.urls import path,include
from . import views

urlpatterns = [
    path('login/',views.login_user,name='login'),
    path('Signup/',views.Signup_user,name='Signup'),
    path('',views.dashboard_user,name='Dashboard'),
    path('logout/',views.logout_User,name='logout'),
    path('about/',views.About_Us,name='About'),
    path('room/',views.Room,name='Room'),
    path('room/',views.Student,name='Student'),
]
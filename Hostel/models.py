from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class UserModel(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     email = models.EmailField(max_length=100,unique=True)
#     password = models.CharField(max_length=100)
#     role = models.ForeignKey('UserType',on_delete=models.CASCADE)
#     joined_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"



class UserType(models.Model):
    user_type = models.CharField(max_length=200)
    def __str__(self):
        return self.user_type
    

from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user  = models.ForeignKey(User , on_delete = models.CASCADE , null = True)
    #image = models.ImageField(default ='default.jpg' , upload_to = 'profile_pics')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    GENDER = [
        ("M", "Male"),
        ("F", "Female"),
        ("N", "Non_binary"),
    ]
    gender = models.CharField(max_length=1, choices=GENDER)


     
    def __str__(self):
       return f'{self.user} Profile'

from django.db import models
from django.contrib.auth.models import User
from adminpanel.models import *

class Cart(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.user.username


class Downloads(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    download_count = models.IntegerField()

    def __str__(self):
        return self.user.username

class Token(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=105, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username



class Contact(models.Model):
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    subject = models.CharField(max_length=1000)
    contact = models.CharField(max_length=1000)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.user.name
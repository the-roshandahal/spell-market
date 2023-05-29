from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from adminpanel.models import *


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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


PAYMENT_CHOICES = (("khalti", "khalti"), ("other", "other"))


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username





class PurchaseSummary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100, unique=True)
    discount = models.IntegerField(
        validators=[MaxValueValidator(10000000), MinValueValidator(10)]
    )
    total_amount = models.IntegerField(
        validators=[MaxValueValidator(10000000), MinValueValidator(10)]
    )

    payment_method = models.CharField(
        max_length=100, choices=PAYMENT_CHOICES, default="khalti", blank=True, null=True
    )

    def __str__(self):
        return self.user.username


class PurchasedTemplate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100)
    download_count = models.IntegerField()
    purchase_summary = models.ForeignKey(PurchaseSummary,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Downloads(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    download_count = models.IntegerField()

    def __str__(self):
        return self.user.username
        
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.user.username




from django.urls import reverse

class SitemapEntry(models.Model):
    url = models.CharField(max_length=200)
    priority = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.url

    def get_absolute_url(self):
        return reverse('sitemap-entry-detail', args=[str(self.pk)])

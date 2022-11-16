from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)
    order = models.IntegerField(null=True)

    def __str__(self):
        return self.category

class Tag(models.Model):
    tag = models.CharField(max_length=100)
    order = models.IntegerField(null=True)

    def __str__(self):
        return self.tag

class Template(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    template_name = models.CharField(max_length=1000)
    template_details = models.TextField()
    template_features = models.TextField()
    template_layout = models.TextField()
    template_price = models.IntegerField()
    released_date = models.DateField(auto_now_add=True)
    version = models.CharField(max_length=100)
    framework = models.CharField(max_length=1000)
    template_image = models.ImageField(null=True, upload_to='blog_images/' )
    template_url = models.URLField(default='#')

    def __str__(self):
        return self.template_name



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


from django.db import models

# Create your models here.
# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)
    category_image = models.ImageField(null=True, upload_to='category_images/' )
    order = models.IntegerField(null=True)
    status = models.IntegerField(null=True, default='1')
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.category
    
class SubCategory(models.Model):
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=100)
    order = models.IntegerField(null=True)
    status = models.IntegerField(null=True, default='1')
    created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.sub_category
    
class ChildCategory(models.Model):
    sub_category= models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    child_category = models.CharField(max_length=100)
    order = models.IntegerField(null=True)
    status = models.IntegerField(null=True, default='1')
    created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.child_category

class Template(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    child_category = models.ForeignKey(ChildCategory, on_delete=models.CASCADE, null=True, blank=True)
    template_name = models.CharField(max_length=1000)
    template_details = models.TextField()
    template_features = models.TextField()
    template_layout = models.TextField()
    template_price = models.IntegerField(max_length=100)
    version = models.CharField(max_length=100)
    framework = models.CharField(max_length=1000)
    template_image = models.ImageField(null=True, upload_to='template_images/' )
    template_url = models.URLField( null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.template_name
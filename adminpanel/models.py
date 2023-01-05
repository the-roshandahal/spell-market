from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category = models.CharField(max_length=100, unique=True)
    category_image = models.ImageField(null=True, upload_to="category_images/")
    order = models.IntegerField(null=True)
    STATUS_CHOICES = (("active", "active"), ("inactive", "inactive"))
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="active")
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.category
    class Meta:
        verbose_name_plural = "1. Category"

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=100, unique=True)
    order = models.IntegerField(null=True)
    STATUS_CHOICES = (("active", "active"), ("inactive", "inactive"))
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="active")
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.sub_category
    class Meta:
        verbose_name_plural = "2. Sub Category"

class ChildCategory(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    child_category = models.CharField(max_length=100)
    order = models.IntegerField(null=True)
    STATUS_CHOICES = (("active", "active"), ("inactive", "inactive"))
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="active")
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.child_category
    class Meta:
        verbose_name_plural = "3. Child Category"

class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag


class Template(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, null=True, blank=True
    )
    child_category = models.ForeignKey(
        ChildCategory, on_delete=models.CASCADE, null=True, blank=True
    )
    tag = models.ManyToManyField(Tag, null=True, blank=True)
    template_name = models.CharField(max_length=1000)
    template_details = models.TextField()
    template_features = models.TextField()
    template_layout = models.TextField()
    template_price = models.IntegerField()
    TAX_CHOICES = (("yes", "yes"), ("no", "no"))
    is_taxable = models.CharField(max_length=20, choices=TAX_CHOICES, default="yes")
    version = models.CharField(max_length=100)
    framework = models.CharField(max_length=1000)
    template_image = models.ImageField(
        null=True, blank=True, upload_to="template_images/"
    )
    template_url = models.URLField(null=True, blank=True)
    template_file = models.FileField(null=True, blank=True, upload_to="template_files/")
    is_featured = models.BooleanField(null=True, default=0)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.template_name


class PromoCode(models.Model):
    promo_code = models.CharField(max_length=10, unique=True)
    TYPE_CHOICES = (("percentage", "percentage"), ("amount", "amount"))
    discount_type = models.CharField(
        max_length=100, null=True, choices=TYPE_CHOICES, default="percentage"
    )
    discount = models.IntegerField(null=True)
    expiry_date = models.DateField(null=True)

    def __str__(self):
        return self.promo_code


class CompanySetup(models.Model):
    logo = models.ImageField(upload_to="company_images/")
    email = models.EmailField()
    contact = models.IntegerField()
    address = models.CharField(max_length=1000)
    facebook_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)


class Blog(models.Model):
    title = models.CharField(max_length=1000)
    blog = models.TextField()
    image = models.ImageField(upload_to="blogs_images/")
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class Partner(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    logo = models.ImageField(upload_to="partner_images/")

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="testimonial_images/")
    company_name = models.CharField(max_length=100)
    testimonial = models.CharField(max_length=100)

    def __str__(self):
        return self.name

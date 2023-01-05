from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

admin.site.site_header = "Admin panel"
from django_summernote.models import Attachment

admin.site.unregister(Attachment)

# Register your models here.
class Description(SummernoteModelAdmin):
    summernote_fields = ("template_details", "template_features", "template_layout")


class BlogField(SummernoteModelAdmin):
    summernote_fields = "blog"


class BlogFields(Description, admin.ModelAdmin):
    list_display = (
        "template_name",
        "released_date",
    )
class CatFields(admin.ModelAdmin):
    list_display = (
        "category",
        "order",
        "status",
    )
class SubCatFields(admin.ModelAdmin):
    list_display = (
        "sub_category",
        "category",
        "order",
        "status",
    )

class ChildCatFields(admin.ModelAdmin):
    list_display = (
        "child_category",
        "sub_category",
        "order",
        "status",
    )

admin.site.register(Category,CatFields)
admin.site.register(SubCategory,SubCatFields)
admin.site.register(ChildCategory,ChildCatFields)
admin.site.register(Template, Description)
admin.site.register(PromoCode)
admin.site.register(CompanySetup)
admin.site.register(Blog, BlogField)
admin.site.register(Partner)
admin.site.register(Testimonial)
admin.site.register(Tag)

from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
admin.site.site_header = "Admin panel"
from django_summernote.models import Attachment

admin.site.unregister(Attachment)

# Register your models here.
class Description(SummernoteModelAdmin):
    summernote_fields = ('template_details','template_features', 'template_layout')


class BlogFields(Description, admin.ModelAdmin):
    list_display = ('template_name', 'released_date',)

admin.site.register(Category)
admin.site.register(Template,Description)

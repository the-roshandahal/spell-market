from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


admin.site.site_header = "Spell Market Admin panel"
# Register your models here.

# admin.site.unregister(Users)
class PrivacyFields(SummernoteModelAdmin):
    summernote_fields = ("privacy_policy","terms_and_condition")

admin.site.register(Cart)
admin.site.register(Downloads)
admin.site.register(Token)
admin.site.register(Contact)
admin.site.register(PurchasedTemplate)
admin.site.register(PurchaseSummary)
admin.site.register(Comments)
admin.site.register(PrivacyAndTerms,PrivacyFields)


admin.site.register(SitemapEntry)
admin.site.register(Faq)


from django.contrib import admin

class DataSetAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        # Prevent deletion of the existing data
        return False

    def save_model(self, request, obj, form, change):
        # Limit the creation of only one data set
        if not obj.pk and Snippet.objects.exists():
            # Data set already exists, don't save the new one
            return
        super().save_model(request, obj, form, change)

admin.site.register(Snippet, DataSetAdmin)

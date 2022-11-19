from django.contrib import admin
from .models import *
admin.site.site_header = "Spell Market Admin panel"
# Register your models here.

# admin.site.unregister(Users)

admin.site.register(Cart)
admin.site.register(Downloads)
admin.site.register(Token)


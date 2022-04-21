from django.contrib import admin

# Register your models here.

from home.models import contact    #added manually
admin.site.register(contact)

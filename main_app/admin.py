from django.contrib import admin

# Register your models here.
from .models import Horse, Feeding

admin.site.register(Horse)
admin.site.register(Feeding)
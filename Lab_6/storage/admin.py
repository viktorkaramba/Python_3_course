from django.contrib import admin

# Register your models here.
from .models import Sections, Goods

admin.site.register(Sections)
admin.site.register(Goods)
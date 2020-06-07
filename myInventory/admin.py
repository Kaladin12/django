from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(alimentos, suplementos)
class ViewAdmin(admin.ModelAdmin):
    pass
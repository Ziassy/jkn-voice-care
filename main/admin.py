# main/admin.py
from django.contrib import admin
from .models import LanguageChoice


class LanguageChoicesAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']


admin.site.register(LanguageChoice, LanguageChoicesAdmin)

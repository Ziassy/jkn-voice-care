from django.contrib import admin
from .models import LanguageChoice, TranslatedMenu, Translation


@admin.register(LanguageChoice)
class LanguageChoiceAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')


@admin.register(TranslatedMenu)
class TranslatedMenuAdmin(admin.ModelAdmin):
    list_display = ('menu_id', 'menu_name')


@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = ('menu', 'language', 'translation')
    list_filter = ('menu', 'language')

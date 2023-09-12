from django.shortcuts import render, redirect
from gtts import gTTS
import os
from django.conf import settings
from .models import LanguageChoice, TranslatedMenu, Translation, SubMenu


def translate(request):
    languages = LanguageChoice.objects.all()

    selected_language = request.GET.get('language', 'id')

    selected_code = selected_language

    translations = Translation.objects.filter(language__code=selected_language)

    # Create a dictionary to store translations for each menu
    menu_translations = {}

    menus = TranslatedMenu.objects.all()

    menu_submenus = {}

    # translation based on the menu ID
    for menu in menus:
        translation = translations.filter(menu__menu_id=menu.menu_id).first()
        menu_translations[menu.menu_name] = translation.translation if translation else 'Translation not available'

        # Retrieve submenus for the current menu
        submenus = SubMenu.objects.filter(menu_id=menu.id)

        # Convert submenus to a list of dictionaries
        submenus_list = [{'submenu_name': submenu.submenu_name}
                         for submenu in submenus]

        # Store the list of submenus in the menu_submenus dictionary
        menu_submenus[menu.menu_id] = submenus_list

    # Pass the selected_menu_id to the template
    return render(request, 'main/template.html', {
        'languages': languages,
        'selected_language': selected_language,
        'selected_code': selected_code,
        'menus': menus,
        'menu_translations': menu_translations,
        'menu_submenus': menu_submenus,
    })


def menu_detail(request, menu_id):
    try:
        menu = TranslatedMenu.objects.get(menu_id=menu_id)
        return render(request, 'main/menu_detail.html', {'menu': menu})
    except TranslatedMenu.DoesNotExist:
        # Redirect to a list view if menu doesn't exist
        return redirect('translate')

from django.shortcuts import render, redirect
from gtts import gTTS
import os
from django.conf import settings
from .models import LanguageChoice, TranslatedMenu, Translation, SubMenu, SubTranslation


def translate(request):
    languages = LanguageChoice.objects.all()

    selected_language = request.GET.get('language', 'id')

    selected_code = selected_language

    translations = Translation.objects.filter(language__code=selected_language)

    # Create a dictionary to store translations for each menu
    menu_translations = {}
    submenu_translations = {}

    menus = TranslatedMenu.objects.all()

    # translation based on the menu ID
    for menu in menus:
        translation = translations.filter(menu__menu_id=menu.menu_id).first()
        menu_translations[menu.menu_name] = translation.translation if translation else 'Translation not available'

        # Filter submenus for the current menu
        submenus = SubMenu.objects.filter(menu_id=menu.menu_id)
        # Translation for submenus based on the submenu ID
        for submenu in submenus:
            submenu_translation = SubTranslation.objects.filter(
                submenu=submenu,
                language__code=selected_language
            ).first()
            submenu_translations[submenu.submenu_name] = submenu_translation.translation if submenu_translation else 'Translation not available'

    if request.method == 'GET':
        for menu_id, translation_text in menu_translations.items():
            if translation_text:
                # Gunakan ID menu sebagai nama file audio
                audio_filename = f'audio-{menu_id}.mp3'
                tts = gTTS(text=translation_text, lang='id')
                audio_path = os.path.join(settings.MEDIA_ROOT, audio_filename)
                tts.save(audio_path)

        for submenu_id, submenu_translation_text in submenu_translations.items():
            if submenu_translation_text:
                audio_filename = f'audio-{submenu_id}.mp3'
                tts = gTTS(text=submenu_translation_text, lang='id')
                audio_path = os.path.join(settings.MEDIA_ROOT, audio_filename)
                tts.save(audio_path)

    print(submenu_translations)

    # Pass the selected_menu_id to the template
    return render(request, 'main/template.html', {
        'languages': languages,
        'selected_language': selected_language,
        'selected_code': selected_code,
        'menus': menus,
        'menu_translations': menu_translations,
        'submenu_translations': submenu_translations
    })


def menu_detail(request, menu_id):
    try:
        menu = TranslatedMenu.objects.get(menu_id=menu_id)
        return render(request, 'main/menu_detail.html', {'menu': menu})
    except TranslatedMenu.DoesNotExist:
        # Redirect to a list view if menu doesn't exist
        return redirect('translate')

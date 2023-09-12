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

        submenus = SubMenu.objects.filter(menu_id=menu.id)
        menu_submenus[menu.menu_name] = submenus

    if request.method == 'GET':
        for menu_id, translation_text in menu_translations.items():
            if translation_text != 'Translation not available':
                # Gunakan ID menu sebagai nama file audio
                audio_filename = f'audio-{menu_id}.mp3'
                tts = gTTS(text=translation_text, lang='id')
                audio_path = os.path.join(settings.MEDIA_ROOT, audio_filename)
                tts.save(audio_path)
            else:
                # Hapus file audio jika terdapat teks 'Translation not available'
                audio_filename = f'audio-{menu_id}.mp3'
                audio_path = os.path.join(settings.MEDIA_ROOT, audio_filename)
                if os.path.exists(audio_path):
                    os.remove(audio_path)
        print(menu_submenus)
        print(menu_translations)

    else:
        print("Tidak tergenerate")

    return render(request, 'main/template.html', {'languages': languages, 'selected_language': selected_language, 'selected_code': selected_code, 'menus': menus, 'menu_translations': menu_translations, 'menu_submenus': menu_submenus})


def menu_detail(request, menu_id):
    try:
        menu = TranslatedMenu.objects.get(menu_id=menu_id)
        return render(request, 'main/menu_detail.html', {'menu': menu})
    except TranslatedMenu.DoesNotExist:
        # Redirect to a list view if menu doesn't exist
        return redirect('translate')

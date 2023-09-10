from django.shortcuts import render
from gtts import gTTS
import os
from django.conf import settings
from .models import LanguageChoice, TranslatedMenu, Translation

def translate(request):
    # Fetch all available languages from your LanguageChoice model
    languages = LanguageChoice.objects.all()

    # Get the selected language from the URL parameter, default to 'id'
    selected_language = request.GET.get('language', 'id')

    selected_code = selected_language

    # Fetch translations for the selected language
    translations = Translation.objects.filter(language__code=selected_language)

    # Create a dictionary to store translations for each menu
    menu_translations = {}

    # Fetch all menus from your TranslatedMenu model
    menus = TranslatedMenu.objects.all()
    
    for menu in menus:
        translation = translations.filter(menu=menu).first()
        menu_translations[menu.menu_id] = translation.translation if translation else 'Translation not available'

    if request.method == 'GET' and 'translate' in request.GET:
        # Use the selected language for text-to-speech
        text = menu_translations.get('your_menu_id', 'Default text if menu_id not found')  # Replace 'your_menu_id' with the actual menu ID you want to use for text-to-speech
        tts = gTTS(text=text, lang=selected_language)
        audio_path = os.path.join(settings.MEDIA_ROOT, 'audio.mp3')
        tts.save(audio_path)
    else:
        print("tidak tergenerate")

    return render(request, 'main/template.html', {'languages': languages, 'selected_language': selected_language, 'selected_code': selected_code, 'menus': menus, 'menu_translations': menu_translations})

from django.shortcuts import render
from gtts import gTTS
import os
from django.conf import settings
from .models import LanguageChoice, TranslatedMenu


def translate(request):
    languages = LanguageChoice.objects.all()
    menus = TranslatedMenu.objects.all()
    selected_language = request.GET.get('language', 'id')

    text = {
        'id': 'Halo dunia',
        'jv': 'Halo jagad',
        'su': 'Halo dunya',
    }[selected_language]

    selected_code = selected_language

    if request.method == 'GET' and 'translate' in request.GET:
        tts = gTTS(text=text, lang='id')
        audio_path = os.path.join(settings.MEDIA_ROOT, 'audio.mp3')
        tts.save(audio_path)
    else:
        print("tidak tergenerate")

    return render(request, 'main/template.html', {'languages': languages, 'selected_language': selected_language, 'text': text, 'selected_code': selected_code, 'menus': menus})

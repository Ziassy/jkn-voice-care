from django.shortcuts import render
from gtts import gTTS
import os
from django.conf import settings  # Import settings


def translate(request):
    languages = ['id', 'jv', 'su']
    selected_language = request.GET.get('language', 'id')
    text = {
        'id': 'Halo dunia',
        'jv': 'Halo jagad',
        'su': 'Halo dunya',
    }[selected_language]

    selected_code = selected_language  # Use the selected_language as the code

    if request.method == 'POST':
        if 'play' in request.POST:
            tts = gTTS(text=text, lang='id')
            audio_path = os.path.join(
                settings.MEDIA_ROOT, 'audio.mp3')  # Use MEDIA_ROOT
            print('ktrigger')
            tts.save(audio_path)

    return render(request, 'main/template.html', {'languages': languages, 'selected_language': selected_language, 'text': text, 'selected_code': selected_code})


# # views.py
# import json
# from django.shortcuts import render
# from django.http import FileResponse, HttpResponseRedirect
# from django.views import View
# from django.utils.translation import activate, gettext_lazy as _
# from gtts import gTTS

# # Define your LANGUAGES variable
# LANGUAGES = [
#     ('en', _('English')),
#     ('id', _('Indonesian')),
#     ('jv', _('Javanese')),
#     ('su', _('Sundanese')),
#     # Add more languages here
# ]


# class PlaySoundView(View):
#     def get_text_for_language(self, language_code):
#         with open('main/translations.json', 'r', encoding='utf-8') as f:
#             translations = json.load(f)

#         text = translations.get(language_code, {}).get(
#             'instruction', 'Hello, world!')
#         return text

#     def get(self, request, language_code):
#         text = self.get_text_for_language(language_code)
#         tts = gTTS(text, lang=language_code)
#         tts.save("output.mp3")
#         return FileResponse(open("output.mp3", "rb"), content_type="audio/mpeg")


# def index(request):
#     translations = get_translations()
#     sound_enabled = True  # Set this value based on your logic
#     return render(request, 'main/template.html', {'translations': translations, 'LANGUAGES': LANGUAGES, 'sound_enabled': sound_enabled})


# def get_translations():
#     with open('main/translations.json', 'r', encoding='utf-8') as f:
#         translations = json.load(f)
#     return translations


# def set_language(request):
#     if request.method == 'POST':
#         language = request.POST.get('language')
#         activate(language)
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

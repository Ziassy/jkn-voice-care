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

    if request.method == 'GET' and 'translate' in request.GET:
        tts = gTTS(text=text, lang='id')
        audio_path = os.path.join(
            settings.MEDIA_ROOT, 'audio.mp3')  # Use MEDIA_ROOT
        print('ktrigger')
        tts.save(audio_path)
    else:
        print("tidak tergenerate")

    return render(request, 'main/template.html', {'languages': languages, 'selected_language': selected_language, 'text': text, 'selected_code': selected_code})

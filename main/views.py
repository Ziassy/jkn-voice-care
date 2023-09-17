from django.shortcuts import render, redirect, get_object_or_404
from gtts import gTTS
import os
from django.conf import settings
from django.urls import reverse
from .models import LanguageChoice, TranslatedMenu, Translation, SubMenu, SubTranslation, DetailSubMenu, DetailSubMenuTranslation


def translate(request):
    languages = LanguageChoice.objects.all()

    selected_language = request.GET.get('language', 'id')

    selected_code = selected_language
    request.session['selected_code'] = selected_code

    translations = Translation.objects.filter(language__code=selected_language)

    # Create a dictionary to store translations for each menu
    menu_translations = {}
    submenu_translations = {}
    detail_submenu_translations = {}

    menus = TranslatedMenu.objects.all()

    # translation based on the menu ID
    for menu in menus:
        translation = translations.filter(menu__menu_id=menu.menu_id).first()
        menu_translations[menu.menu_name] = translation.translation if translation else 'Mohon maaf pada menu ini masih belum tersedia JKN Voice Care'

        # Filter submenus for the current menu
        submenus = SubMenu.objects.filter(menu_id=menu.menu_id)
        # Translation for submenus based on the submenu ID
        for submenu in submenus:
            submenu_translation = SubTranslation.objects.filter(
                submenu=submenu,
                language__code=selected_language
            ).first()
            submenu_translations[submenu.submenu_name] = submenu_translation.translation if submenu_translation else 'Mohon maaf pada menu ini masih belum tersedia JKN Voice Care'

            detail_submenu = DetailSubMenu.objects.filter(submenu=submenu)
            for ds in detail_submenu:
                translation = DetailSubMenuTranslation.objects.filter(
                    detail_submenu=ds,
                    language__code=selected_language
                ).first()
                detail_submenu_translations[ds.title] = translation.translation if translation else 'Mohon maaf pada menu ini masih belum tersedia JKN Voice Care'

    # if request.method == 'GET':
    #     for menu_id, translation_text in menu_translations.items():
    #         if translation_text:
    #             # Gunakan ID menu sebagai nama file audio
    #             audio_filename = f'audio-{menu_id}.mp3'
    #             tts = gTTS(text=translation_text, lang='id')
    #             audio_path = os.path.join(settings.MEDIA_ROOT, audio_filename)
    #             tts.save(audio_path)

    #     for submenu_id, submenu_translation_text in submenu_translations.items():
    #         if submenu_translation_text:
    #             audio_filename = f'audio-{submenu_id}.mp3'
    #             tts = gTTS(text=submenu_translation_text, lang='id')
    #             audio_path = os.path.join(settings.MEDIA_ROOT, audio_filename)
    #             tts.save(audio_path)

    #     for detail_submenu, detail_sub_translation in detail_submenu_translations.items():
    #         if detail_sub_translation:
    #             audio_filename = f'audio-detail-{detail_submenu}.mp3'
    #             tts = gTTS(text=detail_sub_translation, lang='id')
    #             audio_path = os.path.join(settings.MEDIA_ROOT, audio_filename)
    #             tts.save(audio_path)
    # Pass the selected_menu_id to the template
    return render(request, 'main/template.html', {
        'languages': languages,
        'selected_language': selected_language,
        'selected_code': selected_code,
        'menus': menus,
        'menu_translations': menu_translations,
        'submenu_translations': submenu_translations
    })


def submenu_detail(request, detail_url):
    try:
        submenu = get_object_or_404(SubMenu, detail_url=detail_url)
        if submenu.submenu_name:
            detail_submenu = DetailSubMenu.objects.filter(submenu=submenu)

            # Get the selected_language from the session or use 'id' as default
            selected_language = request.GET.get('language', 'id')
            selected_code = request.session.get('selected_code', 'id')

            # Build the URL with the selected_language query parameter
            redirect_url = reverse('submenu_detail', kwargs={
                                   'detail_url': detail_url}) + f'?language={selected_language}'

            detail_submenu_translations = {}

            for ds in detail_submenu:
                translation = DetailSubMenuTranslation.objects.filter(
                    detail_submenu=ds,
                    language__code=selected_language
                ).first()
                detail_submenu_translations[ds.title] = translation.translation if translation else 'Mohon maaf pada menu ini masih belum tersedia JKN Voice Care'
                print(ds)
            return render(request, 'main/submenu_detail.html', {
                'submenu': submenu,
                'detail_submenu': detail_submenu,
                'detail_submenu_translations': detail_submenu_translations,
                'selected_code': selected_code,
            })
        else:
            print("Sub Menu name is empty.")
            return redirect('translate')
    except SubMenu.DoesNotExist:
        return redirect('translate')


def menu_detail(request, detail_url):
    try:
        menu = get_object_or_404(TranslatedMenu, detail_url=detail_url)
        if menu.menu_name:
            return render(request, 'main/menu_detail.html', {'menu': menu})
        else:
            print("Menu name is empty.")
            return redirect('translate')
    except TranslatedMenu.DoesNotExist:
        return redirect('translate')

from django import template

register = template.Library()

@register.simple_tag
def get_sound_enabled(request):
    return request.session.get('sound_enabled', False)

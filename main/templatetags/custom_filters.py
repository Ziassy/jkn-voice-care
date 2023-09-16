from django import template

register = template.Library()


@register.filter(name='dict_lookup')
def dict_lookup(dictionary, key):
    return dictionary.get(key, [])


@register.filter
def get_subtranslation(submenu_translations, submenu_name):
    return submenu_translations.get(submenu_name, "Mohon maaf pada menu ini masih belum tersedia JKN Voice Care")

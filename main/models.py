from django.db import models


class LanguageChoice(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class TranslatedMenu(models.Model):
    menu_id = models.CharField(max_length=50, unique=True)
    menu_name = models.CharField(max_length=50)
    translations = models.ManyToManyField(
        LanguageChoice, through='Translation')
    image_url = models.URLField(
        default='https://s3.us-east-1.amazonaws.com/hyunday-file/1694438095296-Avatar.png')
    detail_url = models.URLField(default="")  # Set the default value to an empty string

    def __str__(self):
        return self.menu_name

    def get_translation_by_code(self, code):
        try:
            translation = self.translations.get(language__code=code)
            return translation.translation
        except Translation.DoesNotExist:
            return 'Translation not available'

class Translation(models.Model):
    menu = models.ForeignKey(TranslatedMenu, on_delete=models.CASCADE)
    language = models.ForeignKey(LanguageChoice, on_delete=models.CASCADE)
    translation = models.TextField()

    def __str__(self):
        return f"{self.menu.menu_name} ({self.language.name})"

from django.db import models

class LanguageChoice(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50)
    translation_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class TranslatedMenu(models.Model):
    menu_id = models.CharField(max_length=50, unique=True)
    menu_name = models.CharField(max_length=50)
    translations = models.ManyToManyField(LanguageChoice, through='Translation')

    def __str__(self):
        return self.menu_name

class Translation(models.Model):
    menu = models.ForeignKey(TranslatedMenu, on_delete=models.CASCADE)
    language = models.ForeignKey(LanguageChoice, on_delete=models.CASCADE)
    translation = models.TextField()

    def __str__(self):
        return f"{self.menu.menu_name} ({self.language.name})"

# models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class LanguageChoice(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

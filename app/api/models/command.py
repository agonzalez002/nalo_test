"""Model related to a command."""

from django.db import models
from django.contrib.auth.models import User


class Command(models.Model):
    """Command model."""

    code = models.CharField(help_text='Command number', max_length=10, unique=True, primary_key=True)
    recipe = models.JSONField(help_text='Command recipe', default=dict)
    command_price = models.IntegerField(help_text='Command price', default=0)

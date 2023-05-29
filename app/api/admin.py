from django.contrib import admin

# Register your models here.
from .models import Command, IceCream


class CommandAdmin(admin.ModelAdmin):
    """Admin model for command."""

    list_display = (
        'code',
    )


class IceCreamAdmin(admin.ModelAdmin):
    """Admin model for icecream."""

    list_display = (
        'flavor',
    )

admin.site.register(Command, CommandAdmin)
admin.site.register(IceCream, IceCreamAdmin)
"""Populate database."""

from django.conf import settings
from django.contrib.auth.models import User

from django.core.management.base import BaseCommand, CommandParser

from api.models import IceCream


class Command(BaseCommand):
    """Populate database."""

    def handle(self, *args, **options):
        """Handle populate db."""

        flavor_1 = IceCream.objects.create(
            flavor='orange_chocolate',
            price=2,
            stock=settings.MAX_STOCK,
        )
        flavor_1.save()
        flavor_2 = IceCream.objects.create(
            flavor='maple_sirup_nuts',
            price=2,
            stock=settings.MAX_STOCK,
        )
        flavor_2.save()
        flavor_3 = IceCream.objects.create(
            flavor='chocolate_mint',
            price=2,
            stock=settings.MAX_STOCK,
        )
        flavor_3.save()
        flavor_4 = IceCream.objects.create(
            flavor='vanilla_strawberry_chocolate',
            price=2,
            stock=settings.MAX_STOCK,
        )
        flavor_4.save()
        flavor_5 = IceCream.objects.create(
            flavor='white_chocolate_raspberry',
            price=2,
            stock=settings.MAX_STOCK,
        )
        flavor_5.save()

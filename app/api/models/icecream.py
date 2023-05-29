"""Models related to an icecream."""

from django.db import models


class IceCream(models.Model):
    """Icecream model."""

    flavor_choice = [
        ('orange_chocolate', 'Chocolat Orange'),
        ('maple_sirup_nuts', 'Sirop d\'érable Noix'),
        ('chocolate_mint', 'Menthe Chocolat'),
        ('vanilla_strawberry_chocolate', 'Vanille Fraise Chocolat'),
        ('white_chocolate_raspberry', 'Chocolat blanc Framboise'),
    ]

    flavor = models.CharField(choices=flavor_choice, help_text="Icecream parfum", max_length=255)
    price = models.IntegerField(default=2, help_text='ice cream scoop price')
    stock = models.IntegerField(default=40, help_text='ice cream scoop quantity')
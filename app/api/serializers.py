"""Serializers."""

from django.conf import settings

from rest_framework import serializers
from .models import Command, IceCream


class CommandSerializer(serializers.ModelSerializer):
    """Command serializer."""

    format_recipe = serializers.SerializerMethodField()

    class Meta:
        model = Command
        fields = ('code', 'command_price', 'format_recipe')

    def get_format_recipe(self, instance):
        """Return formated recipe."""
        formated_data = []
        for key, value in instance.recipe.items():
            formated_data.append({"flavor": key, "number": value})
        return formated_data



class CommandListSerializer(serializers.ModelSerializer):
    """Command list serializer."""

    class Meta:
        model = Command
        fields = ('recipe',)


class IceCreamSerializer(serializers.ModelSerializer):
    """IceCream serializer."""
    filling_rate = serializers.SerializerMethodField()
    flavor_display = serializers.SerializerMethodField()

    class Meta:
        model = IceCream
        fields = ('flavor', 'flavor_display', 'filling_rate', 'id')

    def get_filling_rate(self, instance):
        """Return filling rate for ice cream."""
        stock_max = settings.MAX_STOCK
        rate = (100 * instance.stock) / stock_max
        return rate

    def get_flavor_display(self, instance):
        """Return flavor display value."""
        return instance.get_flavor_display()

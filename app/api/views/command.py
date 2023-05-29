"""Command api views."""

import ast
from typing import Any
import uuid
from django import http

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from ..serializers import CommandSerializer, CommandListSerializer
from ..models import Command, IceCream


class CommandViewSet(viewsets.ModelViewSet):
    """ViewSet on Command model."""

    queryset = Command.objects.all()
    serializer_class = CommandSerializer

    @action(detail=False, methods=['GET'], permission_classes=[IsAdminUser])
    def command_listing(self, request):
        """"List endpoint"""
        queryset = self.get_queryset()
        serialized_data = CommandListSerializer(queryset, many=True)
        return Response(serialized_data.data)

    @action(detail=False, methods=['POST'], permission_classes=[AllowAny])
    def new_command(self, request):
        """Create endpoint"""
        recipe = request.data.get('recipe', dict)
        code = uuid.uuid4().hex[:10]
        price = 0
        for flavor, number in recipe.items():
            icecream = IceCream.objects.get(flavor=flavor)
            if icecream.stock == 0:
                print(f"Attention le pot de glace ({icecream.get_flavor_display()}) est vide. Pensez à le remplir.")
            price += icecream.price * int(number)
            icecream.stock -= int(number)
            if icecream.stock < 0:
                msg = f'Il n\'y a plus assez de boule de {icecream.get_flavor_display()} pour valider votre commande'
                return Response({'error': msg}, status=424)
            icecream.save()
        Command.objects.create(
            code=code,
            recipe=recipe,
            command_price=price,
        )
        return Response({'price': price, 'command_code': code})

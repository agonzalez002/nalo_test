"""IceCreame api view."""

from django.conf import settings

from rest_framework import viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from ..serializers import IceCreamSerializer
from ..models import IceCream


class IceCreamViewSet(viewsets.ModelViewSet):
    """ViewSet for ice cream model."""

    queryset = IceCream.objects.all()
    serializer_class = IceCreamSerializer

    def update(self, request, pk=None):
        item = self.get_object()
        item.stock = settings.MAX_STOCK
        item.save()
        msg = f'Le pot de glace ({item.get_flavor_display()}) est de nouveau plein.'
        return Response({"success": msg})
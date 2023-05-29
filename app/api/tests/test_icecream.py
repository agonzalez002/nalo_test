import pytest

from django.test import TestCase

from rest_framework.test import APIRequestFactory

from api.views.icecream import IceCreamViewSet
from api.models import IceCream

factory = APIRequestFactory()


@pytest.mark.django_db
class TestIceCreamViewSet(TestCase):
    """Test class for /api/icecream."""

    def test_icecream_state(self):
        icecream = IceCream.objects.create(
            id=1,
            flavor="flavor_1",
            price=2,
            stock=20,
        )
        icecream.save()
        request = factory.get('/api/icecream/1/', content='application/json')
        view = IceCreamViewSet.as_view(actions={'get': 'retrieve'})
        response = view(request, pk=1)
        expected = {
            'id': 1,
            'flavor': 'flavor_1',
            'flavor_display': 'flavor_1',
            'filling_rate': 50.0
            }
        assert expected == response.data

    def test_icecream_refill(self):
        icecream = IceCream.objects.create(
            id=1,
            flavor="flavor_1",
            price=2,
            stock=20,
        )
        icecream.save()
        request = factory.put('/api/icecream/1/', content='application/json')
        view = IceCreamViewSet.as_view(actions={'put': 'update'})
        response = view(request, pk=1)
        expected = {'success': 'Le pot de glace (flavor_1) est de nouveau plein.'}
        assert expected == response.data
        icecream_refilled = IceCream.objects.get(id=1)
        assert icecream_refilled.stock == 40



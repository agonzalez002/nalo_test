import pytest

from django.contrib.auth.models import User
from django.test import TestCase

from rest_framework.test import APIRequestFactory

from api.views.command import CommandViewSet
from api.models import Command, IceCream

factory = APIRequestFactory()


@pytest.mark.django_db
class TestCommandViewSet(TestCase):
    """Test class for /api/command."""

    def test_command_listing(self):
        command1 = Command.objects.create(
            code="abcd",
            recipe={"icecream1": 2, "icecream2": 42},
            command_price=88,
        )
        command1.save()
        command2 = Command.objects.create(
            code="efgh",
            recipe={"icecream1": 1, "icecream2": 2},
            command_price=6,
        )
        command2.save()
        command3 = Command.objects.create(
            code="ijkl",
            recipe={"icecream1": 5, "icecream2": 1},
            command_price=12,
        )
        command3.save()
        request = factory.get('/api/command/command_listing/', '', content='application/json')
        view = CommandViewSet.as_view(actions={'get': 'command_listing'})
        response = view(request)
        expected = [
            {
                "recipe": {'icecream1': 2, 'icecream2': 42},
            },
            {
                "recipe": {'icecream1': 1, 'icecream2': 2},
            },
            {
                "recipe": {'icecream1': 5, 'icecream2': 1},
            },
        ]
        assert expected == response.data

    def test_new_command(self):
        icecream1 = IceCream.objects.create(
            id=1,
            flavor="flavor_1",
            price=2,
            stock=40,
            )
        icecream1.save()
        icecream2 = IceCream.objects.create(
            id=2,
            flavor="flavor_2",
            price=2,
            stock=40,
            )
        icecream2.save()
        data = {
            "recipe": {'flavor_1': 2, 'flavor_2': 4},
        }
        request = factory.post('/api/command/new_command/', data=data, format='json', content='application/json')
        view = CommandViewSet.as_view(actions={'post': 'new_command'})
        response = view(request)
        assert response.data.get('price') == 12

    def test_get_command(self):
        command1 = Command.objects.create(
            code="abcdef",
            recipe={"icecream1": 2, "icecream2": 42},
            command_price=88,
        )
        command1.save()
        request = factory.get('/api/command/abcdef/', content='application/json')
        view = CommandViewSet.as_view(actions={'get': 'list'})
        response = view(request)
        expected = [
            {
                'code': 'abcdef',
                'format_recipe': [
                    {
                        'flavor': 'icecream1',
                        'number': 2,
                    },
                    {
                        'flavor': 'icecream2',
                        'number': 42,
                    }
                ],
                'command_price': 88,
            },
        ]
        assert expected == response.data

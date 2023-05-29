import pytest

from api.models import Command, IceCream


@pytest.fixture
def create_command(db):
    """Provide a factory to create a command."""
    def _create_command(**kwargs):
        test_command = Command(**kwargs)
        test_command.save()
        return test_command

    yield _create_command


@pytest.fixture
def create_icecream(db):
    """Provide a factory to create an icecream."""
    def _create_icecream(**kwargs):
        test_icecream = IceCream(**kwargs)
        test_icecream.save()
        return test_icecream

    yield _create_icecream

import pytest
from pytest_factoryboy import register

from ..factories import UserFactory

register(UserFactory)


@pytest.fixture
def test_user():
    user = UserFactory()
    user.save()
    user.set_password("testing123")
    user.save()
    return user

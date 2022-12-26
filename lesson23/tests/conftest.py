from pytest_factoryboy import register

from tests.factories import AdsFactory, UserFactory

pytest_plugins = 'tests.fixtures'


register(AdsFactory, _name="ad")
register(UserFactory, _name="user")

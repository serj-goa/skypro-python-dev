import factory.django
from ads.models import Ad
from user.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = 'test name'
    password = 'test12345'

class AdsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "testing name"
    price = 100
    description = "testing description"
    is_published = False

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import *
from .validators import DomainValidator, BirthDayValidator


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class UserAdSerializer(serializers.ModelSerializer):
    total_ads = serializers.IntegerField()
    location = serializers.SlugRelatedField(
        slug_field='name',
        many=True,
        read_only=True
    )

    class Meta:
        model =User
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        slug_field='name',
        many=True,
        required=False,
        queryset=Location.objects.all()
    )
    email = serializers.EmailField(validators=[DomainValidator('rambler.ru'),
                                               UniqueValidator(queryset=User.objects.all())])
    birth_date = serializers.DateField(validators=[BirthDayValidator()])

    def is_valid(self, *, raise_exception=False):
        self._location = self.initial_data.pop('location')
        super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])

        for loc in self._location:
            object, _ = Location.objects.get_or_create(name=loc)
            user.location.add(object)

        user.save()
        return user

    def save(self):
        user = super().save()
        user.set_password(user.password)

        user.location.clear()
        for loc in self._location:
            odject, _ = Location.objects.get_or_create(name=loc)
            user.location.add(odject)
        user.save()
        return user

    class Meta:
        model = User
        fields = "__all__"

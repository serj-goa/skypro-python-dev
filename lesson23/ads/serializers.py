from rest_framework import serializers
from .models import *

class AdSerializer(serializers.ModelSerializer):
    # author = serializers.CharField()
    # category = serializers.CharField()
    author = serializers.SlugRelatedField(read_only=True, slug_field='id' )
    category = serializers.SlugRelatedField(read_only=True, slug_field='id')

    class Meta:
        model = Ad
        fields = '__all__'


class AdUpdateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'name', 'image']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ('id', 'name',)


class SelectionDetailSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field='id', read_only=True)
    items = AdSerializer(
        many=True
        )

    class Meta:
        model = Selection
        fields = '__all__'
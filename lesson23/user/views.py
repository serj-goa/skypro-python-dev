from django.db.models import Count, Q
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from user.models import Location, User
from user.serializers import LocationSerializer, UserSerializer, UserAdSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserAdDetailView(ListAPIView):
    queryset = User.objects.annotate(total_ads=Count('ad', filter=Q(ad__is_published=True)))
    serializer_class = UserAdSerializer

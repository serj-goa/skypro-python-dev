from django.http import JsonResponse
from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     UpdateAPIView,
                                     RetrieveAPIView,
                                     DestroyAPIView)
from ads.serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from user.permissions import AdUpdateDeletePermission


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def get(self, request, *args, **kwargs):
        ad_cat = request.GET.get('cat')
        if ad_cat:
            self.queryset = self.queryset.filter(category__id__exact=ad_cat)

        ad_name = request.GET.get('text')
        if ad_name:
          self.queryset = self.queryset.filter(name__icontains=ad_name)

        ad_city = request.GET.get('location')
        if ad_city:
            self.queryset = self.queryset.filter(
                author__location__name__icontains=ad_city)

        price_from = request.GET.get('price_from', 0)
        price_to = request.GET.get('price_to', 100000)
        if price_from or price_to:
            self.queryset = self.queryset.filter(
                price__range=[price_from, price_to])

        return super().get(request, *args, **kwargs)


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, AdUpdateDeletePermission]


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, AdUpdateDeletePermission]


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, AdUpdateDeletePermission]


class AdImageView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateImageSerializer


class SelectionListView(ListAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer


class SelectionCreateView(CreateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer


class SelectionDetailView(RetrieveAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionDetailSerializer




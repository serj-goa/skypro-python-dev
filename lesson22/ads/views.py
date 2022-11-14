import json

from django.http import JsonResponse, Http404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ads, Categories


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class AdView(View):
    def get(self, request):
        data = Ads.objects.all()

        response = []

        for ad in data:
            response.append(
                {
                    "id": ad.id,
                    "name": ad.name,
                    "author": ad.author,
                    "price": ad.price,
                    "description": ad.description,
                    "address": ad.address,
                    "is_published": ad.is_published
                }
            )

        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})

    def post(self, request):
        data = json.loads(request.body)

        ad = Ads.objects.create(
            name=data['name'],
            author=data['author'],
            description=data['description'],
            price=data['price'],
            address=data['address'],
            is_published=data['is_published']
        )

        return JsonResponse(
            {
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
                "description": ad.description,
                "address": ad.address,
                "is_published": ad.is_published
            },
            json_dumps_params={'ensure_ascii': False}
        )


@method_decorator(csrf_exempt, name="dispatch")
class CategoryView(View):
    def get(self, request):
        data = Categories.objects.all()

        response = []

        for category in data:
            response.append(
                {
                    "id": category.id,
                    "name": category.name
                }
            )

        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})

    def post(self, request):
        data = json.loads(request.body)

        category = Categories.objects.create(
            name=data['name'],
        )

        return JsonResponse(
            {
                "id": category.id,
                "name": category.name,
            },
            json_dumps_params={'ensure_ascii': False}
        )


@method_decorator(csrf_exempt, name="dispatch")
class AdDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        try:
            ad = self.get_object()
        except Http404:
            return JsonResponse({'Error': 'Not found'}, status=404)

        return JsonResponse(
            {
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
                "description": ad.description,
                "address": ad.address,
                "is_published": ad.is_published
            },
            json_dumps_params={'ensure_ascii': False}
        )


@method_decorator(csrf_exempt, name="dispatch")
class CategoryDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwars):
        try:
            category = self.get_object()
        except Http404:
            return JsonResponse({'Error': 'Not found'}, status=404)

        return JsonResponse(
            {
                "id": category.id,
                "name": category.name
            },
            json_dumps_params={'ensure_ascii': False}
        )

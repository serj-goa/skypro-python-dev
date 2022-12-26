from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from ads import views
from rest_framework import routers

from ads.views import CategoryViewSet

router = routers.SimpleRouter()
router.register('cat', CategoryViewSet)


urlpatterns = [

    path('ad/', views.AdListView.as_view()),
    path('ad/create/', views.AdCreateView.as_view()),
    path('ad/<int:pk>/image/', views.AdImageView.as_view()),
    path('ad/<int:pk>/', views.AdDetailView.as_view()),
    path('ad/<int:pk>/update/', views.AdUpdateView.as_view()),
    path('ad/<int:pk>/delete/', views.AdDeleteView.as_view()),

    path('selection/', views.SelectionListView.as_view()),
    path('selection/create/', views.SelectionCreateView.as_view()),
    path('selection/<int:pk>/', views.SelectionDetailView.as_view()),

]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
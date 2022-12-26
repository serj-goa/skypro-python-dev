from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user import views

from user.views import LocationViewSet, UserViewSet

router = routers.SimpleRouter()
router.register('location', LocationViewSet)
router.register('user', UserViewSet)

urlpatterns = [

    path('user/Z/', views.UserAdDetailView.as_view()),

    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view())
]

urlpatterns += router.urls
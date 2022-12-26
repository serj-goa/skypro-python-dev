from django.contrib import admin
from django.urls import path, include
from ads.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('', include("ads.urls")),
    path('', include('user.urls'))
]

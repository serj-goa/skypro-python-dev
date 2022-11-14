from django.urls import path

from ads import views


urlpatterns = [
    path('', views.index),
    path('ad/', views.AdView.as_view()),
    path('ad/<int:pk>/', views.AdDetailView.as_view()),
    path('cat/', views.CategoryView.as_view()),
    path('cat/<int:pk>/', views.CategoryDetailView.as_view()),
]

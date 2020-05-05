from django.urls import path

from .import views

urlpatterns = [
    path('', views.allcourse, name='course'),
]


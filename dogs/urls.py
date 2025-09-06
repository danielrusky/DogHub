from django.urls import path

from dogs.apps import DogsConfig
from dogs.views import index, contact

app_name = DogsConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
]
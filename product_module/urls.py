from django.urls import path
from .views import index, meow
urlpatterns = [
    path('', index),
    path('meow', meow),
]
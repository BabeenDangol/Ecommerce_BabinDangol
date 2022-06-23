from django.urls import path
from .views import index, meow , index2
urlpatterns = [
    path('', index),
    path('meow', meow),
    path('index2', index2),
]
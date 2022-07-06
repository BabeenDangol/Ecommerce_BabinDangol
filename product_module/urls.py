from django.urls import path
from .views import index, meow , index, test
urlpatterns = [
    path('', index),
    path('meow', meow),
    path('index', index),
    path('test', test),
]
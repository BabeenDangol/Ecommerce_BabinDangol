from django.urls import path
from .views import   index,  collection , shoes, contact,racing_boots
urlpatterns = [
    path('', index),
    path('index.html', index),
    path('collection.html', collection),
    path('shoes.html', shoes),
    path('contact.html', contact),
    path('racing boots.html',racing_boots),
]
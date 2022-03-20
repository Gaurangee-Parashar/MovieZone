from django.urls import path
from . import consumer

ws_urlpatterns = [
    path('ws/some_url/', consumer.WSConsumer.as_asgi())
]
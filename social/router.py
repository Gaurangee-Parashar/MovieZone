from django.urls import path
from . import consumer

ws_urlpatterns = [
    path('ws/chat/@me/<str:id>', consumer.ChatConsumer.as_asgi())
]
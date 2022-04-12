from django.urls import path
from . import views

urlpatterns = [
    path('chat/@me/<str:user_id>', views.chat)
]
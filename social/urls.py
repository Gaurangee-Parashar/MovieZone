from django.urls import path
from . import views

urlpatterns = [
    path('delete_review/<str:id>', views.delete_review, name='delete_review')
]
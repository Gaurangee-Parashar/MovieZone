from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/<str:id>', views.movies, name='movies'),
    path('person/<str:id>', views.person, name='person'),
    path('search/', views.search, name='search')

]
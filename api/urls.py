from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('get_reviews/<str:id>/', views.getReviews),
    path('new_review/', views.newReview),
    path('delete_review/<str:id>/', views.deleteReview),
    path('add_liked_movie/', views.add_liked_movie)
]
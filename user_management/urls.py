from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutView, name='logout'),
    path('profile/<str:id>', views.profile, name="profile")
]
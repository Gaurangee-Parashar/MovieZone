from sys import path_hooks
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('', include('user_management.urls')),
    path('', include('social.urls')),
    path('api/', include('social.api.urls'))

]
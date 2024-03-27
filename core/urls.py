
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('chat/', include('chatapp.urls')),
    path('rooms/', include('roomapp.urls')),
]

from django.contrib import admin
from django.urls import path, include
from galeria.views import index

urlpatterns = [
    path('', include('galeria.urls')),
    path('admin/', admin.site.urls),
]

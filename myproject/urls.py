# myproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('django_q/', include('django_q.urls')),
    path('', include('myapp.urls')),  # Inclure les URLs de l'application
]

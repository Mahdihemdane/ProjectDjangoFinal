# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('myapp/', views.myapp_view, name='myapp'),
    # Autres URLs spécifiques à l'application...
]

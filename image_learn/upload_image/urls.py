from django.urls import path
from . import views

urlpatterns = [
    path('imagefield/', views.display)
]

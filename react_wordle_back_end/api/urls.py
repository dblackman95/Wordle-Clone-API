from django.urls import path
from . import views

urlpatterns = [
    path('solutions', views.solutions),
    path('letters', views.letters),
]
from django.urls import path
from .views import Hello_world, AboutView

urlpatterns = [
    path('', Hello_world.as_view(), name="home"),
    path('about', AboutView.as_view(), name="about"),
]

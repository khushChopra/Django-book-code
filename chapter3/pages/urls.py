from django.urls import path
from .views import Hello_world, AboutView, KhushView

urlpatterns = [
    path('', Hello_world.as_view(), name="home"),
    path('about', AboutView.as_view(), name="about"),
    path('khush', KhushView, name="khush"),
]

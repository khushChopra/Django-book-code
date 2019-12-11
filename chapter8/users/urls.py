from django.urls import path, include
from .views import firstView

urlpatterns = [
    path('', firstView),
]

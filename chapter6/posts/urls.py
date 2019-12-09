from django.contrib import admin
from django.urls import path
from .views import HomePageView, DetailPageView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('', HomePageView.as_view() , name='home'),
    path('detail/<int:pk>', DetailPageView.as_view() , name='detail'),
    path('detail/<int:pk>/update', BlogUpdateView.as_view() , name='update'),
    path('detail/<int:pk>/delete', BlogDeleteView.as_view() , name='delete'),
    path('post/new', BlogCreateView.as_view(), name="post_new")
]

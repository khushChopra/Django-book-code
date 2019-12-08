from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class DetailPageView(DetailView):
    model = Post
    template_name = 'detail.html'

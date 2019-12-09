from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class DetailPageView(DetailView):
    model = Post
    template_name = 'detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = "__all__"

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('home')
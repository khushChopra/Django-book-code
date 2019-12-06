from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class Hello_world(TemplateView):
    template_name = "home.html"

class AboutView(TemplateView):
    template_name = "about.html"
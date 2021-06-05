from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class Blog(TemplateView):
    template_name = "about/blog.html"

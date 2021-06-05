from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class About(TemplateView):
    template_name = "about/about_us.html"

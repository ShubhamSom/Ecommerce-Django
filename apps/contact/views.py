from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class Contact(TemplateView):
    template_name = "contact/contact_us.html"

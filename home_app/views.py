from django.shortcuts import render

# Create your views here.

# class HomePageView:
#     template_name = 'homepage.html'


def index(request):
    return render(request, template_name='homepage.html')


from django.urls import path


# from home_app.views import HomePageView
from . import views

urlpatterns = [
    # path('', HomePageView.as_view(), name='home'),
    path('', views.index, name="home_url")
]
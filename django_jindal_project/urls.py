"""django_jindal_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path('', include('home_app.urls')),
    path('home/', include('home_app.urls')),
    path('shop/', include('apps.shop.urls')),
    # path(r'^blog/', include('blog.urls')),
    # path(r'user/', include('apps.user.urls')),
    path(r'about/', include('apps.about.urls')),
    path(r'contact/', include('apps.contact.urls')),
    path(r'blog/', include('apps.blog.urls')),

    path(r'tmp/', TemplateView.as_view(template_name='temp-templates/testing_file.html'), name='test'),
    path(r'tmp1/', TemplateView.as_view(template_name='temp-templates/tf1.html'), name='test1'),
    path(r'tmp2/', TemplateView.as_view(template_name='temp-templates/tf2.html'), name='test2'),
]

#  Add URL maps to redirect the base URL to our application
# from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='', permanent=True)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

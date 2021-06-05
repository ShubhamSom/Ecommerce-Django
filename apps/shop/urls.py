from django.urls import path, re_path
# from .views import ProductList, ProductDetail, product_detail
from . import views

# app_name = 'shop'
# more suggestions
# https://stackoverflow.com/questions/11494483/django-class-based-view-how-do-i-pass-additional-parameters-to-the-as-view-meth
urlpatterns = [
    # path('', views.Shop.as_vi ew(), name="contact_url")
    # path('men/', Category.as_view(type='men'), name='category_men_url'),
    # path('women/', Category.as_view(type='women'), name='category_women_url'),
    # path('kids/', Category.as_view(type='kids'), name='category_kids_url'),
    # path('fresh-arrivals/', Category.as_view(type='arrival'), name='category_arrival_url')
    # re_path(r'^(?P<slug>[\w-]+)/$', ProductList.as_view(), name='category_url'),  # now no need to pass category_type name

    path('home/', views.frontpage, name='front_url'),  # now no need to pass category_type name
    path('categories/', views.categories, name='categories_url'),  # now no need to pass category_type name
    path('<slug:slug>/', views.category_detail, name='category_url'),  # now no need to pass category_type name
    path('<slug:category_slug>/<slug:slug>/', views.product_detail, name='product_detail_url'),  # now no need to pass category_type name
    # path('<slug:category_type>/', ProductList.as_view(), name='product_list_by_category_url'),  # now no need to pass category_type name
]
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView

from .models import Product, Category

#
# class Shop(TemplateView):
#     pass
#
#
# class ProductList(generic.ListView):  # ProductListByCategory
#     model = Product
#     template_name = "category_base.html"
#
#     # slug_url_kwarg = 'category_type'
#     # print(slug_url_kwarg)
#     def get_queryset(self):
#         return get_object_or_404(self, slug=self.kwargs['slug'])
#
#     def get_context_data(self, **kwargs):
#         print('slug Entered :', self.kwargs['slug'])
#         context = super(ProductList, self).get_context_data(**kwargs)
#         return context  # to template for rendering


def frontpage(request):
    products = Product.objects.all()
    print('prod, ', products)
    context = {
        'products': products,
    }
    return render(request, 'shop/shop.html', context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    context = {
        'category': category,
        'products': products,
    }
    # return render(request, 'shop/shop.html', context)
    return render(request, 'shop/category_detail.html', context)


# class ProductDetail:
#     pass


def product_detail(request, category_slug, slug):
    # try:
    #     product = Product.objects.filter(slug=slug)[0]
    # except IndexError:
    #     product = None
    #     from django.http import Http404
    #     raise Http404
    product = get_object_or_404(Product, category__slug=category_slug, slug=slug)
    # print('hey', Product.objects.filter(category__slug=category_slug).filter(slug=slug))
    context = {
        'product': product,
    }
    return render(request, 'shop/product_detail.html', context)


def categories(request):
    category_list = Category.objects.all()
    context = {
        'categories': category_list,
    }
    return render(request, 'shop/categories.html', context)

from .models import Category


# make it accessible to index.html or navbar.html
def menu_category_list(request):
    categories = Category.objects.filter(parent=None)
    context = {
        'menu_categories': categories,
    }
    return context

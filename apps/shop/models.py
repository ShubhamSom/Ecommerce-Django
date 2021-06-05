from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    parent = models.ForeignKey("self", related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, primary_key=True)
    order = models.PositiveIntegerField(db_index=True, default=0)

    class Meta:
        ordering = ('order',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_url', args=[self.slug])


class Product(models.Model):
    parent = models.ForeignKey("self", related_name='variants', on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    # all the other product fields
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # price = models.FloatField()
    image = models.ImageField(upload_to='img/product/', default='')
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        args = []
        kwargs = {'category_slug': self.category.slug, 'slug': self.slug}
        return reverse('product_detail_url', args=args, kwargs=kwargs)



from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    CategoryImage = models.ImageField(upload_to='category_img', blank=True)
    CategoryDescription = models.TextField(blank=True)

    class Meta:
        ordering = ('categoryName',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('shop02:products_by_category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.categoryName)

class Product(models.Model):
    productName = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    productImage = models.ImageField(upload_to='product_img', blank=True)
    productDescription = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    productAvailable = models.BooleanField(default=True)
    productPrice = models.DecimalField(max_digits=20, decimal_places=2)
    productStock = models.IntegerField()
    productCreatedAt = models.DateField(auto_now_add=True)
    productUpdateAt = models.DateField(auto_now=True)


    def get_url(self):
        return reverse('shop02:productDetail', args=[self.category.slug, self.slug])

    class Meta:
        ordering =('productName',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.productName)
from django.db import models
from django.conf import settings
from .managers import ProductManager 
from django.urls import reverse
# Create your models here.

CURRENCY = settings.CURRENCY



class News(models.Model):
    name = models.CharField(max_length=300)
    preview = models.TextField()
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    images = models.ImageField(blank=True)
    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.name

class NewsImage(models.Model):
    news = models.ForeignKey(News, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to = 'news/')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'NewsImages'

    def __str__(self):
        return self.news.name

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slag = models.SlugField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name

class ProductSize(models.Model):
    size = models.CharField(max_length=10)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'ProductSizes'

    def __str__(self):
        return self.size


class Product(models.Model):
    name = models.CharField(max_length=200)
    article = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    sizes = models.ManyToManyField(to=ProductSize,related_name="prodSize")
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    discount = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    final_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    preview = models.CharField(max_length=200)
    description = models.TextField()
    active = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    productManager = ProductManager()
    

    class Meta:
        verbose_name_plural = 'Products'

    def get_absolute_url(self):
        return reverse('ecommerce:productdetails',args=[self.id])

    def save(self, *args, **kwargs):
        self.final_price = self.discount if self.discount > 0 else self.price
        super().save(*args, **kwargs)

    def tag_final_price(self):
        return f'{self.final_price} {CURRENCY}'
    tag_final_price.short_description = 'Price'

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, related_name='images', on_delete=models.CASCADE)
    images = models.ImageField(upload_to = 'products/')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    class Meta: 
        verbose_name_plural = 'ProductImages'

    def __str__(self):
        return self.product.name

class Delivery(models.Model):
    deliveryOption = models.CharField(max_length=200)
    deliveryPrice = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    class Meta: 
        verbose_name_plural = 'Deliveries'
    def __str__(self):
        return self.deliveryOption



class ProductsOrder(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()
    price =  models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    class Meta: 
        verbose_name_plural = 'ProductsOrders'
    def __str__(self):
        return self.products.name


class Order(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    address = models.TextField()
    agree = models.BooleanField(default=True)
    delivery = models.ForeignKey(Delivery, on_delete=models.RESTRICT)
    productsOrder = models.ManyToManyField(ProductsOrder, related_name='productsOrder')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    class Meta: 
        verbose_name_plural = 'Orders'
    
    def __str__(self):
        return self.fullName




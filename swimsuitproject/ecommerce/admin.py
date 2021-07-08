from django.contrib import admin
from .models import News, NewsImage, ProductImage, Product, ProductSize, Delivery, Order, ProductsOrder, Category
# from .forms import ProductForm
# Register your models here.

class NewsImageAdmin(admin.StackedInline):
    model = NewsImage
 
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImageAdmin]
 
    class Meta:
       model = News
 
@admin.register(NewsImage)
class NewsImageAdmin(admin.ModelAdmin):
    pass




class ProductImagesAdmin(admin.StackedInline):
    model = ProductImage
 
 
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['name', 'category', 'tag_final_price', 'active']
    list_select_related = ['category']
    list_filter = ['active', 'category']
    search_fields = ['name']
    list_per_page = 50
    fields = ['active', 'name', 'category','article','preview','description', 'price', 'discount', 'tag_final_price', 'sizes']
    autocomplete_fields = ['category']
    readonly_fields = ['tag_final_price']
    class Meta:
       model = Product

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     inlines = [ProductImagesAdmin]
#     # form = ProductForm
#     class Meta:
#        model = Product
      
 
@admin.register(ProductImage)
class ProductImagesAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    pass


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductsOrder)
class ProductsOrderAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

# admin.site.register(News, NewsAdmin)

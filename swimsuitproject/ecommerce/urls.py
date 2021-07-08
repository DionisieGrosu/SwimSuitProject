from django.urls import path
from . import views

app_name = "ecommerce"

urlpatterns = [
    path('', views.index),
    path('catalog', views.catalog),
    path('catalog/<int:id>', views.catalogDetail, name = 'productdetails'),
    path('addToCart', views.addToCart, name='addToCart'),
    path('getCartProducts', views.getCartProducts, name="getCartProducts"),
    path('changeCartItemQty', views.changeCartItemQty, name="changeItemQty"),
    path('deleteFromCart', views.deleteFromCart, name="deleteFromCart"),
    path('contacts', views.contacts),
]

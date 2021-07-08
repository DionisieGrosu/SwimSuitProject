from django import forms
from .models import Product, ProductSizes

class ProductForm(forms.ModelForm):
    sizes = forms.MultipleChoiceField(
        choices = tuple((q['id'], q['size']) for q in ProductSizes.objects.values())
        # choices = (ProductSizes.objects.get()),
    )
    class Meta:
        model = Product
        fields = ['name', 'article', 'sizes','price','discount','preview', 'description', 'images']
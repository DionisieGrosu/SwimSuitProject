
from django.shortcuts import render
from .models import News, Product, ProductImage, ProductSize, Delivery
from django.http import JsonResponse, Http404, HttpResponseBadRequest
from django.core import serializers
from django.urls import reverse
import json
# from .serializers import ProductSerializer
import random
# Create your views here.


def index(request):
    news = News.objects.all()[:3]
    if(news):
        context = {
            'news' : news
        }
    else:
        context = {
            'news' : []
        }
      
    return render(request, 'partials/index.html', context)


def catalog(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'partials/catalog.html', context)


def catalogDetail(request, id):
    
    if request.is_ajax != False:
        product = Product.objects.get(pk = id)
        deliceryOptions = Delivery.objects.all()
        relatedProducts = random.sample(list(Product.objects.all()), len(list(Product.objects.all())) if len(list(Product.objects.all())) < 4 else 4)
        # print({product})
        # productSizes = ProductSize.objects.filter()
        if product:
            # productJSON = serializers.serialize('json', product, fields=('name','article','sizes','price','discount','description'))
            # productImagesJSON = serializers.serialize('json', ProductImage.objects.filter(product = product),fields=('images'))
            context = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'article' : product.article,
                    'sizes': [size.size for size in ProductSize.objects.filter(prodSize = product)],
                    'price': product.final_price,
                    'discount': product.discount,
                    'description': product.description,
                    'images': [image.images.url for image in ProductImage.objects.filter(product = product)],
                },
                'relatedProducts': [{**{'name': relatedProduct.name,'preview': relatedProduct.preview, 'price' : relatedProduct.final_price, 'discount': relatedProduct.discount}, **{'images': [image.images.url for image in relatedProduct.images.all()], 'url': relatedProduct.get_absolute_url()}} for relatedProduct in relatedProducts]
                
                # 'relatedProducts': [{relatedProduct} for relatedProduct in relatedProducts]
            }
            # print(serializers.serialize('json',relatedProducts, fields=('name','final_price','price','discount','preview', 'images'), use_natural_foreign_keys=True, indent=4))
            # print(ProductSerializer(instance=relatedProducts))
            # print([size.size for size in ProductSize.objects.filter(prodSize = product)])
            # print([[image.images.url for image in relatedProduct.images.all()] for relatedProduct in relatedProducts])
            print([{**{'name': relatedProduct.name,'preview': relatedProduct.preview, 'price' : relatedProduct.final_price, 'discount': relatedProduct.discount}, **{'images': [image.images.url for image in relatedProduct.images.all()]}} for relatedProduct in relatedProducts])
            return JsonResponse(context)
        else:
            raise Http404("Product does not exist")
    else:
        raise Http404("Product does not exist")


def addToCart(request):
    print(request.session)
    if request.GET:
        productId = request.GET.get('productId')
        size = request.GET.get('size')
        if 'productsCart' in request.session:
            product = Product.objects.get(pk = int(productId))
            deliveryOptions = Delivery.objects.all()
            cartHasItem = False
            # print(request.session['productsCart'])
            for cartItem in request.session['productsCart']:
                if cartItem['id'] == int(productId):
                    cartHasItem = True
                    break

            if cartHasItem == False:
                productResponse = {
                    'id': product.id,
                    'name': product.name,
                    'preview': product.preview,
                    'price': str(product.final_price),
                    'size': size,
                    'qty': 1,
                    'article': product.article,
                    'image': [image.images.url for image in product.images.all()[:1]],
                    'changeQtyUrl': reverse('ecommerce:changeItemQty'),
                    'deleteItemUrl': reverse('ecommerce:deleteFromCart')
                }
                # print( request.session['productsCart'])
                request.session['productsCart'].append(productResponse)
                request.session.modified = True
        else:
            product = Product.objects.get(pk = int(productId))
            deliveryOptions = Delivery.objects.all()
            productResponse = {
                'id': product.id,
                'name': product.name,
                'preview': product.preview,
                'price': str(product.final_price),
                'size': size,
                'qty': 1,
                'article': product.article,
                'image': [image.images.url for image in product.images.all()[:1]],
                'changeQtyUrl': reverse('ecommerce:changeItemQty'),
                'deleteItemUrl': reverse('ecommerce:deleteFromCart')
            }
            deliveryChoises = {
                'deliveryOptions': [{'id': delivery.id, 'delivery': delivery.deliveryOption, 'deliveryPrice': str(delivery.deliveryPrice)} for delivery in deliveryOptions]
            }
            # print( request.session['productsCart'])
            request.session['productsCart'] = [productResponse]
            request.session.modified = True
            request.session['deliveryOptions'] = [deliveryChoises]
            request.session.modified = True
        
        
        return JsonResponse({'productsCart': request.session['productsCart'], 'deliveryOptions':request.session['deliveryOptions']})
    else:
        return HttpResponseBadRequest()
    



def contacts(request):
    return render(request, 'partials/contacts.html')


def getCartProducts(request):
    # del request.session['productsCart']
    # request.session.modified = True
    # deliveryOptions = Delivery.objects.all()
    if 'productsCart' in request.session:
        return JsonResponse({'productsCart': request.session['productsCart'], 'deliveryOptions': request.session['deliveryOptions']})
    else:
        raise Http404()

def changeCartItemQty(request):
    if request.is_ajax:
        # print(json.load(request))
        requestData = json.load(request)
        for product in request.session['productsCart']:
            # print(product['id'])
            # print(productId)
            if int(product['id']) == int(requestData['productId']):
                product['qty'] = requestData['qty']
                request.session.modified = True
                break
    else:
        return HttpResponseBadRequest()
    return JsonResponse({'productsCart': request.session['productsCart']})


def deleteFromCart(request):
    if request.is_ajax:
        # print(json.load(request))
        requestData = json.load(request)
        
        for index, product in enumerate(request.session['productsCart'], start=0):
            # print(product['id'])
            # print(productId)
            if int(product['id']) == int(requestData['productId']):
                del request.session['productsCart'][index]
                request.session.modified = True
                break
    else:
        return HttpResponseBadRequest()
    return JsonResponse({'productsCart': request.session['productsCart']})
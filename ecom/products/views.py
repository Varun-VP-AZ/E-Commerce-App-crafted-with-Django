from django.shortcuts import render
from products.models import Product

# Create your views here.


def get_product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {'product': product}

    if request.GET.get('size'):
        size = request.GET.get('size')
        price = product.get_product_price_by_size(size)
        context['selected_size'] = size
        context['updated_price'] = price
        print(price)

    return render(request, 'product/product.html', context=context)

"""
    try:  # to prevent random slugs from opening(if someone puts wrong slugs in url)
        product = Product.objects.get(slug=slug)
        context = {'product': product}

        if request.GET.get('size'):
            size = request.GET.get('size')
            price = product.get_product_price_by_size(size)
            context['selected_size'] = size
            context['updated_price'] = price
            print(price)

        return render(request, 'product/product.html', context={'product': product})

    except Exception as e:
        print(e)
        
        
        
        
        
        
        
    product = Product.objects.get(slug=slug)
    context = {'product': product}

    if request.GET.get('size'):
        size = request.GET.get('size')
        price = product.get_product_price_by_size(size)
        context['selected_size'] = size
        context['updated_price'] = price
        print(price)

    return render(request, 'product/product.html', context=context)
"""
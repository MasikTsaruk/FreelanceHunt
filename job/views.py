from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from math import ceil


def unfiltred(request):
    products = Product.objects.all()
    p = Paginator(products, 10)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    for i in page_obj.object_list:
        print(i.productCode)
    return render(request, 'Page.html', {'products': products, 'page_obj': page_obj})


def filtred(request, page):
    page = page*10
    products = Product.objects.all()[page-10:page]
    total_pages = ceil(Product.objects.count()/10) - 1
    filtred_products_ids = []
    filtred_products = []
    must_be = ['9', '3', '8', '2']
    for product in products:
        code = str(product.productCode)
        code_list = [element for element in code]
        for i in must_be:
            if i in code_list:
                filtred_products_ids.append(''.join(code_list))
                break
    for product_id in filtred_products_ids:
        product = Product.objects.get(productCode=product_id)
        filtred_products.append(product)
    print(len(filtred_products))
    return render(request, 'Filtred_page.html', {'products': filtred_products,
                                                 'page': int(page/10),
                                                 'total_pages': total_pages,})

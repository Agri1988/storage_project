from django.shortcuts import render, render_to_response
from django.template import RequestContext, Template, Context
from django.template.loader import render_to_string, get_template
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.http import JsonResponse

from .models import Product, Products
from documents_app.models import Document
from .forms import ProductForm, CategoryForm
# Create your views here.

def all_products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products_app/all_products.html', context)


def product_detail(request, product_id, document_id = None, storage_id=None):
    if product_id == '0':
        product = None
    else:
        product = Product.objects.get(id=product_id)
    print(document_id, storage_id)
    product_form = ProductForm()
    if request.method != 'POST':
        product_form = ProductForm(instance=product)
    else:
        product_form = ProductForm(instance=product,data=request.POST)
        if product_form.is_valid():
            new_product = product_form.save()
            product_id = new_product.id
            return HttpResponseRedirect(reverse('documents_app:document_detail', args=[document_id, product_id, storage_id]))
    context = {'product_id':product_id,'product_form':product_form, 'ducument_id':document_id, 'storage_id':storage_id,
               }
    return render(request, 'products_app/add_product_in_document.html', context)


def products_in_document_change_data(request, products_in_document_id):
    if request.method == 'POST':
        update_line = Products.objects.get(id=products_in_document_id)
        update_line.count = request.POST['count']
        update_line.save(update_fields=['count'])
    return JsonResponse({})


def add_category(request):
    print(request.GET)
    if request.method != 'POST':
        print('get')
        category_form = CategoryForm()
        context = {'category_form': category_form}
        template = get_template('products_app/add_category.html')
        return HttpResponse(template.render(context, request))
    else:
        print(request.POST)
        category_form = CategoryForm(data=request.POST)
        if category_form.is_valid():
            print('valid')
            new_category = category_form.save()
            new_category_id = new_category.id
            new_category_name = new_category.name
        data_dict = {'new_category_id':new_category_id, 'new_category_name':new_category_name}
        return JsonResponse(data_dict)
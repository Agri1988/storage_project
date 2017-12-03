from django.shortcuts import render
from datetime import date
from decimal import Decimal
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


from products_app.models import ProductMovement, Product, Products
from documents_app.models import Document
from store_app.models import Storage

def products_in_storage(request, filter_name = None,filter_value=None):
    d= {filter_name:filter_value}
    if filter_name == None:
        products = ProductMovement.objects.all()
    else:
        products = ProductMovement.objects.filter(**d)
        #products = ProductMovement.objects.filter(product__product_price=1.53)
        print(products)
    product_total_price = [product.count * product.product.product_price for product in products]
    result = zip(products, product_total_price)

    return render(request, 'reports_app/base_report.html', {'result':result})


def products_remnants(request, document_id = None, document_date = date.today().strftime('%d.%m.%Y'), storage_id = None):
    document_date = document_date.split('.')
    document_date.reverse()
    document_date = '-'.join(document_date)
    if storage_id != None:
        movement_entries = ProductMovement.objects.filter(date__lte=document_date).filter(storage=storage_id)
    else:
        movement_entries = ProductMovement.objects.filter(date__lte=document_date)
    products = Product.objects.all()
    remnants_of_products = {}
    for product in products:
        product_id_inloop = product.id
        for product_entry in movement_entries:
            product_count = product_entry.count
            if (product_entry.operation_type =='remove'):
                product_count = product_count * (-1)
            elif product_entry.operation_type =='move':
                product_count = product_count * (-1)
                # product_count_rem = product_count * (-1)
                # product_count_add = product_count
            if (product.id == product_entry.product_id) and (product_entry.operation_status == 1):
                if product_id_inloop not in remnants_of_products:
                    remnants_of_products[product_id_inloop] = product_count
                else:
                    remnants_of_products[product_id_inloop] += product_count
    #print(remnants_of_products)
    context = {'products':products, 'remnants_of_products':remnants_of_products, 'document_id':document_id,
               "document_date":document_date, 'storage_id':storage_id}
    return render(request, 'reports_app/base_report.html', context)


def add_product_to_outgoing_document(request ):
    if request.method == 'POST':
        new_products_in_document = Products(document=Document.objects.get(id=request.POST['input_document_id']),
                                            product=Product.objects.get(id=request.POST['input_product_id']),
                                            count= Decimal(request.POST['product_count']))

        new_products_in_document.save()
    return JsonResponse({})

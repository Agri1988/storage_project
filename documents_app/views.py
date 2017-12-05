from django.shortcuts import render
from .models import Document
from .form import DocumentForm
from products_app.models import Products, Product, ProductMovement
from products_app.forms import ProductForm, ProductsForm
from store_app.forms import StorageForm
from store_app.models import Storage
from decimal import Decimal

# Create your views here.

def all_documents(request):
    documents = Document.objects.all()
    products_in_documents = Products.objects.all()
    summary_cost = {}
    for document in documents:
        for product_in_document in products_in_documents:
            if product_in_document.document_id == document.id:
                if (document.id not in summary_cost.keys()):
                    summary_cost[document.id] = product_in_document.count * product_in_document.product.product_price
                else:
                    summary_cost[document.id] += product_in_document.count * product_in_document.product.product_price
    context = {'documents': documents,'summary_cost':summary_cost}
    return render(request, 'documents_app/all_documents.html', context)

def document_detail(request, document_id, product_id = None, storage_id = None, to_storage_id = None):
    print(request.POST)
    if product_id and storage_id != None:
        insert_products_in_document = Products(document=Document.objects.get(id=document_id),
                                        product=Product.objects.get(id=product_id), count=0)
        insert_products_in_document.save()

    if document_id == '0':
        document = None
        products_forms_and_id = []
    else:
        document = Document.objects.get(id=document_id)
        products_in_document = Products.objects.filter(document_id=document_id)
        #print(products_in_document)
        products_in_document_forms = [ProductsForm(instance=product) for product in products_in_document]
        products_in_document_id = [product.id for product in products_in_document]
        products_forms_and_id = zip(products_in_document_forms,products_in_document_id)
        #print(products_in_document_forms, '\n', products_in_document_id)
    product_form = ProductForm()

    if request.method != 'POST':
        document_form = DocumentForm(instance=document)
    else:
        document_form = DocumentForm(instance=document,data=request.POST)

        if document_form.is_valid():
            new_document = document_form.save()

            entry_in_product_movement = ProductMovement.objects.filter(document_id=document_id)
            def check_operation_status(entry_in_product_movement=entry_in_product_movement):
                print(entry_in_product_movement[0].operation_status)
                if len(entry_in_product_movement) != 0 and entry_in_product_movement[0].operation_status != \
                        document.document_status_execute:

                    for entry in entry_in_product_movement:
                        entry.operation_status = document.document_status_execute
                        entry.save(update_fields=['operation_status'])
                        print('changed status')

            try:
                if document.document_status_execute == 1:
                    values_product_in_documents = list(entry_in_product_movement.values_list('product_id', flat=True))
                    print(values_product_in_documents, '\n')
                    for index, product in enumerate(products_in_document):
                        if (len(entry_in_product_movement) == 0) or (product.product_id not in values_product_in_documents):
                            def add_entry(storage=document.storage, document_type=document.document_type):
                                new_entry_into_product_movement = ProductMovement()
                                new_entry_into_product_movement.count = product.count
                                new_entry_into_product_movement.product = Product.objects.get(id=product.product_id)
                                new_entry_into_product_movement.document = Document.objects.get(id=document_id)
                                new_entry_into_product_movement.date = document.date
                                new_entry_into_product_movement.operation_type = document_type
                                new_entry_into_product_movement.operation_status = document.document_status_execute
                                new_entry_into_product_movement.storage = storage
                                new_entry_into_product_movement.save()
                            if product.document.document_type=='move':
                                add_entry(document_type='remove')
                                add_entry(storage=document.to_storage, document_type='add')
                            else:
                                add_entry()
                            print("проведен")
                        elif product.product_id in values_product_in_documents:
                            update_data = entry_in_product_movement.filter(product_id=product.product_id)
                            for element in update_data:
                                if product.count != element.count:
                                    element.count = product.count
                                    element.save(update_fields=['count'])
                    else:
                        check_operation_status()
                else:
                    check_operation_status()
                    print("Не проведен")
            except Exception as exception:
                print ('excepted', exception)

            document_id = new_document.id
    context = {'document_form':document_form, 'document_id':document_id, 'products_forms_and_id': products_forms_and_id,
               'product_form':product_form}
    return render(request, 'documents_app/document_detail.html', context)

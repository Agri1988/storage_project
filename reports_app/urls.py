
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.products_remnants, name='product_remnants'),
    url(r'^(?P<filter_name>[a-z]*_*[a-z]*_*[a-z]*)/(?P<filter_value>[a-z0-9.-]*)$', views.products_in_storage,
        name='products_in_storage'),

    url(r'^(?P<document_date>[0-9]{2}.[0-9]{2}.[0-9]{4})/(?P<document_id>\d+)/(?P<storage_id>\d+)$',
        views.products_remnants, name='product_remnants_filter'),
    url(r'^add_product_to_outgoing_document$', views.add_product_to_outgoing_document,
        name='add_product_to_outgoing_document'),
]



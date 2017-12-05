
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.all_products, name='all_products'),
    url(r'^(?P<product_id>\d+)$', views.product_detail, name='product_detail'),
    url(r'^(?P<product_id>\d+)/(?P<document_id>\d+)/(?P<storage_id>\d+)$', views.product_detail, name='product_detail'),
    url(r'^products_in_document/(?P<products_in_document_id>\d+)$', views.products_in_document_change_data,
        name='products_in_document_change_data'),
    url(r'^get_category_form$', views.add_category, name='add_category'),
]
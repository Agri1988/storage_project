
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.all_documents, name='all_documents'),
    url(r'^price_ticket/(?P<document_id>\d+)/$', views.price_ticket, name='price_ticket'),
    url(r'^(?P<document_id>\d+)$', views.document_detail, name='document_detail'),
    url(r'^(?P<document_id>\d+)/(?P<product_id>\d+)/(?P<storage_id>\d+)$', views.document_detail, name='document_detail'),
]
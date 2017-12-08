from django.conf.urls import url
from partners_app import views

urlpatterns = [
    url(r'^$', views.all_partners, name='all_partners'),
    url(r'^get_partner_form/$', views.add_partner, name='add_partner'),

]
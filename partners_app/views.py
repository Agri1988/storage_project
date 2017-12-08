from django.shortcuts import render
from partners_app.models import Partner
from django.template.loader import render_to_string, get_template
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from .forms import PartnerForm

def all_partners (request):
    partners = Partner.objects.all()
    context = {'partners':partners}
    return render(request, 'partners_app/all_partners.html', context)
# Create your views here.


def add_partner(request):
    print(request.GET)
    if request.method != 'POST':
        print('get')
        partner_form = PartnerForm()
        context = {'partner_form': partner_form}
        template = get_template('partners_app/add_partner.html')
        return HttpResponse(template.render(context, request))
    else:
        print(request.POST)
        partner_form = PartnerForm(data=request.POST)
        if partner_form.is_valid():
            print('valid')
            new_partner = partner_form.save()
            new_partner_id = new_partner.id
            new_partner_name = new_partner.short_name
        data_dict = {'new_partner_id':new_partner_id, 'new_partner_name':new_partner_name}
        return JsonResponse(data_dict)

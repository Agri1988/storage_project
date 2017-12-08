from django.shortcuts import render
from partners_app.models import Partner

def all_partners (request):
    partners = Partner.objects.all()
    context = {'partners':partners}
    return render(request, 'partners_app/all_partners.html', context)
# Create your views here.

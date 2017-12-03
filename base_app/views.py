from django.shortcuts import render
from datetime import date

# Create your views here.
def base (request):
    return render(request, 'base_app/base.html', {'today':date.today().strftime('%d.%m.%Y')})
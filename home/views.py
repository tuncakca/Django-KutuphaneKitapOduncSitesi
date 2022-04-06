from django.shortcuts import render
from django.http import HttpResponse

from home.models import Setting

# Create your views here.

def index(request):
    setting = Setting.objects.get(pk=1)
    text = "Merhaba Django"
    context = {'setting': setting, 'page': 'Home'}
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    text = "Hakkimizda yazisi"
    context = {'setting': setting, 'page': 'Hakkimizda'}
    return render(request, 'about.html', context)
   
def referenslarimiz(request):
    setting = Setting.objects.get(pk=1)
    text = "Referanslarimiz yazisi"
    context = {'setting': setting, 'page': 'Referanslarimiz'}
    return render(request, 'references.html', context)

def iletisim(request):
    setting = Setting.objects.get(pk=1)
    text = "İletişim yazisi"
    context = {'setting': setting, 'page': 'iletisim'}
    return render(request, 'contact.html', context)
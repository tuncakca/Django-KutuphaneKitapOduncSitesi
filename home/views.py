from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from home.models import ContactFormMessage, ContactFormu, Setting
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
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
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajiniz basari ile gonderilmistir")
            return HttpResponseRedirect('/iletisim')


    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context = {'setting': setting, 'form': form, 'page': 'iletisim'}
    return render(request, 'contact.html', context)
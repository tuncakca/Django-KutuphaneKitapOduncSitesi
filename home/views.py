from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from books.models import Book, Category, Comment, Images

from home.models import ContactFormMessage, ContactFormu, Setting
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from home.forms import SearchForm
# Create your views here.

def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Book.objects.all()[:4]
    category = Category.objects.all()
    daybooks = Book.objects.all()[:4]
    lastbooks = Book.objects.all().order_by('-id')[:4]
    randombooks = Book.objects.all().order_by('?')[:4]

    text = "Merhaba Django"
    context = {'setting': setting, 'page': 'Home', 'sliderdata': sliderdata, 'category': category,
    'daybooks': daybooks,
    'lastbooks': lastbooks,
    'randombooks': randombooks,
     }
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

def category_books(request,id, slug):
    category = Category.objects.all()
    categorydata = Category.object.get(pk=id)
    books = Book.objects.filter(category_id=id)
    context = {'books' : books, 'category': category, 'categorydata': categorydata}
    return render(request,'book_detail.html', context)

def book_detail(request, id, slug):
    category = Category.objects.all()
    book = Book.objects.get(pk=id)
    images = Images.objects.filter(book_id=id)
    comments = Comment.objects.filter(book_id=id, status='True')
    context = {'book' : book, 'category': category, 'images': images, 'comments': comments,}

    
    return render(request,'book_detail.html', context)

def book_search(request):
   if request.method == 'POST':
      form = SearchForm(request.POST)
      if True: #if form.is_vaild():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            books = Book.objects.filter(title_icontains=query)
            context = {
               'books': books,
                'category': category,
            }
            return render(request, 'books_search.html', context)

         
   return HttpResponseRedirect('/')
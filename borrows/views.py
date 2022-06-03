from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from borrows.models import BorrowCartForm, BorrowCart
from books.models import Category

# Create your views here.

def index(request):
    return HttpResponse("Borrow app")

@login_required(login_url='/login') # Check login
def addtocart(request, id):
    url = request.META.get('HTTP_REFERER')
    checkbook = BorrowCart.objects.filter(book_id=id)
    if checkbook:
        control = 1
    else:
        control = 0

    form = BorrowCartForm(request.POST)
    if form.is_valid() and not control:
        current_user = request.user

        data = BorrowCart()
        data.user_id = current_user.id
        data.book_id = id
        data.returndate = form.cleaned_data['returndate']
        data.bookdate = form.cleaned_data['bookdate']

        data.save()

        messages.success(request, "Kitap başarı ile ödünç alınmıştır.")
        return HttpResponseRedirect(url)

    else:
        print("errors : {}".format(form.errors))
        return HttpResponse("Kitap zaten istek listenizde ekli")
    #return HttpResponseRedirect(url)


@login_required(login_url='/login') # Check login
def borrowcart(request):
    category = Category.objects.all()
    current_user = request.user
    borrowcart1 = BorrowCart.objects.filter(user_id = current_user.id)
    context = {'borrowcart1': borrowcart1, 'category': category, }
    return render(request, 'borrowcart_books.html', context)

@login_required(login_url='/login') # Check login
def deletefromcart(request, id):
    BorrowCart.objects.filter(id=id).delete()
    messages.success(request, "Kitap listenizden silinmiştir")
    return HttpResponseRedirect("/borrowcart")
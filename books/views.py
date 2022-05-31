from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from books.models import Category, CommentForm, Comment, Book
from django.contrib.auth.decorators import login_required
from home.forms import SearchForm

def index(request):
   return  HttpResponse("My Book Page")

@login_required(login_url='/login')
def addcomment(request,id):
   url = request.META.get('HTTP_REFERER')  # get last url
   #return HttpResponse(url)
   if request.method == 'POST':  # check post
      form = CommentForm(request.POST)
      if form.is_valid():
         current_user = request.user

         data = Comment()  # create relation with model
         data.subject = form.cleaned_data['subject']
         data.comment = form.cleaned_data['comment']
         data.rate = form.cleaned_data['rate']
         data.ip = request.META.get('REMOTE_ADDR')
         data.book_id=id
         current_user= request.user
         data.user_id=current_user.id
         data.save()  # save data to table
         messages.success(request, "Yorumunuz başarı ile kayıt edildi.")
         return HttpResponseRedirect(url)

   return HttpResponseRedirect(url)





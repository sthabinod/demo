from django.shortcuts import render
from django.http import HttpResponseRedirect
from . models import Book

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from django.urls import resolve
from django.contrib.auth.models import User
from django.conf import settings

from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.contrib import messages




# Create your views here.

@login_required
def addBook(request):
    return render(request,"list.html")

@login_required
def book(request):
    return render(request,"addBookButton.html")


    
@login_required
def sell(request):
    return render(request,"book_registration.html")
# def donate(request):
#     return HttpResponseRedirect("/addbook")

@login_required
def donate(request):
    return render(request,"donate_book_register.html")




@login_required
def added(request):
    book_name=request.POST['book_name']
    bookowner=request.user.id
    category=request.POST['category']
    writer=request.POST['writer']
    desc=request.POST['description']
    image=request.FILES['book_photo']
    condition=request.POST['condition']
    actualPrice=int(request.POST['actual_price'])
    sellingPrice=int(request.POST['selling_price'])
    publication=request.POST['publication']

    displaySellingPrice=sellingPrice+(10*sellingPrice/100)

    # url_name=resolve(request.path).url_name
    # if(url_name == 'added_sell'):
    #     donation=request.POST['false']
    # else:
    #     donation=request.POST['true']

    

    book=Book(bname=book_name, bookowner=bookowner, category=category, writer=writer, description=desc, image=image, condition=condition, actual_price=actualPrice, selling_price=sellingPrice, publication=publication, display_selling_price=displaySellingPrice)
    book.save()
    messages.success(request,"Successfully Added Book for Sale")
    return HttpResponseRedirect('sell')





    

    





@login_required
def addeddonate(request):
    book_name=request.POST['book_name']
    bookowner=request.user.id
    category=request.POST['category']
    writer=request.POST['writer']
    desc=request.POST['description']
    image=request.FILES['book_photo']
    condition=request.POST['condition']
    publication=request.POST['publication']

    donation=True




    book=Book(bname=book_name, bookowner=bookowner, category=category, writer=writer,donation=donation, description=desc, image=image, condition=condition, actual_price=0, selling_price=0, publication=publication, display_selling_price=0)
    book.save()
    messages.success(request,"Successfully Added Book for Donation")
    return HttpResponseRedirect('donate')





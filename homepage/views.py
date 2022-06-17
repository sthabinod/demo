from django.shortcuts import render
from django.http import Http404
from .models import HomeSlide
from django.views.generic import DetailView
from registration.models import Profile

    


def book_list_view(request):

    context={
        'object':"sjkdl",
        'homeslide':"slide",
        'latest':"last_four",
        'featured':"featured",
        'recommended': "recommended",
        'extra':"extra",
        'd_of_day':"d_of_day",

    }
    return render(request,"home.html",context)



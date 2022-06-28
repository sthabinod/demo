"""hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views


urlpatterns = [
    #  path('',views.addBook, name='addBook' ),
    path('',views.book, name='addBook' ),



    path('book',views.book,name="book"),

    path('sell',views.sell,name="sell"),
    path('add_book',views.added, name='added_book'),

    path('donate',views.donate,name="donate"),
    path('add_book_donate',views.addeddonate,name='add_book_donate'),

    



   







]

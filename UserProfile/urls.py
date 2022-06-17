from django.urls import path
from . import views
urlpatterns = [
    path('', views.profile, name='profile'),
    #path('editprofile/update/', views.infoupdate, name='update'),
]

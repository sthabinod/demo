from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def profile(request):
    userprofile1 = User.objects.get(id=request.user.id)
    return render(request, 'profile/Profile.html', {'userProfile': userprofile1})



# def editprofile(request):
#     userprofile1 = UserProfile.objects.get(id=4)
#     return render(request, 'editprofile.html', {'userProfile': userprofile1})



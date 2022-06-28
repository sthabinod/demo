from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.core.mail import send_mail
from registration.forms import SignUpForm
from registration.tokens import account_activation_token
from django.conf import settings





def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()           
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'prabhav/registration/signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'prabhav/registration/account_activation_sent.html')


def activate(request, uidb64, token):
    pass





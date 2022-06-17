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

            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('prabhav/registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'token': account_activation_token.make_token(user),
            })
            from_email=settings.EMAIL_HOST_USER
            to_email=[user.email]
            send_mail(subject=subject,from_email=from_email,recipient_list=to_email,message=message,fail_silently=False)

            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'account/registration/signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'prabhav/registration/account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        # uid: force_text(urlsafe_base64_encode(force_bytes(user.pk)))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'prabhav/registration/account_activation_invalid.html')






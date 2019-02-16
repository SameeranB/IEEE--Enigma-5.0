from django.shortcuts import render
from .forms import UserForm, LoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View, FormView
from django.conf import settings
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.http import HttpResponse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from users.models import CustomUser
from django.template.loader import render_to_string

import requests
from django.contrib import messages



# Create your views here.

# Make template views



class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def signup_view(request):
    registered = False
    trigger = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        # Check if the forms are valid
        if user_form.is_valid():



            # Hashing the password
            user = user_form.save()
            user.set_password(user.password)
            user.is_active = False
            current_site = get_current_site(request)


            # Sending activation link in terminal
            # user.email_user(subject, message)
            mail_subject = 'Activate Your enigma account!!'
            message = render_to_string('LoginSignup/acc_active_email.html', {
                'user': user, 'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            # email_from = settings.EMAIL_HOST_USER
            to_email = [user_form.cleaned_data.get('email')]
            # send_mail(subject, message, email_from, to_email)

            email = EmailMessage(mail_subject, message, to=[to_email])
            email.content_subtype = 'html'
            email.send()
            registered = True
            # return HttpResponse('please confirm your email address by activating')
        trigger = True
    else:
        user_form = UserForm()

    return render(request, 'LoginSignup/Signup.html',
                  {'registered': registered, 'user_form': user_form, 'errors': user_form.errors, 'trigger': trigger})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
        token = account_activation_token.make_token(user)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
       # login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')



class LoginView(FormView):
    template_name = 'index.html'
    form_class = LoginForm

    def form_valid(self, form):

        user = authenticate(username=form.cleaned_data['Username'], password=form.cleaned_data['Password'])
        login(self.request, user)
        return HttpResponseRedirect(reverse('index'))

    def get_success_url(self):
        return render(self.request, 'index.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['LoginForm'] = LoginForm
        return context


class LogoutView(LoginRequiredMixin, View):

    login_url = '/LoginSignup/Login'
    redirect_field_name = '/index.html'

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


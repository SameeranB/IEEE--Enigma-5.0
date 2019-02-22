from smtplib import SMTPAuthenticationError

from django.shortcuts import render
from .forms import UserForm, LoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View, FormView
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from .tokens import account_activation_token
from django.http import HttpResponse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from users.models import CustomUser
from django.template.loader import render_to_string
from django.shortcuts import render_to_response
from django.template import RequestContext

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
            user.save()


            # Sending activation link in terminal
            # user.email_user(subject, message)
            mail_subject = 'Activate Your Enigma Account | IEEE VIT'
            message = render_to_string('LoginSignup/acc_active_email.html', {
                'user': user.username,
                'domain': 'enigma5.herokuapp.com',
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })

            to_email = [user_form.cleaned_data.get('email')]

            email = EmailMessage(mail_subject, message,'sameeranbandishti@ieee.org', to=[to_email])
            email.content_subtype = 'html'

            try:
                email.send()
            except SMTPAuthenticationError:
                return render(request, 'SMTPError.html')
            registered = True

        else:
            pass

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
        return render(request, 'LoginSignup/after_signup_f.html')
    else:
        return HttpResponse('Activation link is invalid!')



class LoginView(FormView):
    template_name = 'index.html'
    form_class = LoginForm
    invalid = False

    def form_valid(self, form):

        user = authenticate(username=form.cleaned_data['Username'], password=form.cleaned_data['Password'])
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(self.request, 'NotConfirmed.html')
        else:
            self.invalid = True
            return render(self.request, 'index.html', context={'LoginForm':LoginForm, 'invalid':self.invalid})

    def get_success_url(self):
        return render(self.request, 'index.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['LoginForm'] = LoginForm
        context['invalid'] = self.invalid
        return context

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))


class LogoutView(LoginRequiredMixin, View):

    login_url = '/LoginSignup/Login'
    redirect_field_name = '/index.html'

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))



def SendRem(request):
    usrs = CustomUser.objects.filter(is_active=False).values_list('email', flat=True)
    mail_subject = 'Activate Your Enigma Account | IEEE VIT'
    message = render_to_string('LoginSignup/reminder.html')

    email = EmailMessage(mail_subject, message, 'sameeranbandishti@ieee.org', to=usrs)
    email.content_subtype = 'html'

    email.send()


class IncorrectSent(TemplateView):
    template_name = 'LoginSignup/IncorrectSent.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class NotConf(TemplateView):
    template_name = 'NotConfirmed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def handler404(request, exception, *args, **argv):
    response = render_to_response("404.html")
    response.status_code = 404
    return response


def handler500(request, exception, *args, **argv):
    response = render_to_response("500.html")
    response.status_code = 500
    return response
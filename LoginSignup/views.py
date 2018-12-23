from django.shortcuts import render
from .forms import UserForm, LoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View, FormView
from django.conf import settings
from django.core.mail import send_mail
from .tokens import account_activation_token
from django.http import HttpResponse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.models import User


# Create your views here.

# Make template views

class IndexView(TemplateView):
    template_name = 'index.html'

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def signup_view(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        # Check if the forms are valid
        if user_form.is_valid():

            # Hashing the password
            user = user_form.save()
            user.set_password(user.password)
            user.is_active = False
            email = user.email
            current_site = get_current_site(request)
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = account_activation_token.make_token(user)
            body = ("Dear {}, \n"
                    "Thanks for registering with engima click on the link below to activate your account. \n"
                    "http://{}/activate/{}/{}".format(user.username, current_site.domain,
                                                      urlsafe_base64_encode(force_bytes(user.pk)),
                                                      account_activation_token.make_token(user)))

            send_mail('enigma', str(body), settings.EMAIL_HOST_USER, [email], fail_silently = False)
            user.save()
            # Making the one to one relation
            # Checking for Profile Picture
            registered = True
            return HttpResponse('please confirm your email address by activating')

        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'LoginSignup/Signup.html',
                  {'registered': registered, 'user_form': user_form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')



class LoginView(FormView):
    template_name = 'LoginSignup/Login.html'
    success_url = '/'
    form_class = LoginForm

    def form_valid(self, form):
        username = form.cleaned_data['Username']
        password = form.cleaned_data['Password']
        user = authenticate(username=username, password=password)
        login(self.request, user)

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
        return HttpResponseRedirect(reverse("index.html"))

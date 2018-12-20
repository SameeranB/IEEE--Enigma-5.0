from django.shortcuts import render
from .forms import UserForm, LoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View, FormView

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
            user.save()
            # Making the one to one relation
            # Checking for Profile Picture
            registered = True

        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'LoginSignup/Signup.html',
                  {'registered': registered, 'user_form': user_form})

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

from django.shortcuts import render
from .forms import UserForm
from .forms import UserProfileForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

# Make template views
def index_view(request):
    return render(request,'index.html')


def signup_view(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        user_profile_form = UserProfileForm(data=request.POST)

        # Check if the forms are valid
        if user_form.is_valid() and user_profile_form.is_valid():

            # Hashing the password
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            # Making the one to one relation
            profile = user_profile_form.save(commit=False)
            profile.user = user
            # Checking for Profile Pictures
            if 'ProfilePicture' in request.FILES:
                profile.ProfilePicture = request.FILES['ProfilePicture']
            # Saving the model-form
            profile.save()

            registered = True

        else:
            print(user_form.errors, user_profile_form.errors)
    else:
        user_form = UserForm()
        user_profile_form= UserProfileForm()

    return render(request, 'LoginSignup/Signup.html',
                  {'registered': registered, 'user_form': user_form, 'user_profile_form': user_profile_form})


def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("User Inactive")
        else:
            return HttpResponse("Invalid Details")
    else:
        return render(request,'LoginSignup/Login.html')

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
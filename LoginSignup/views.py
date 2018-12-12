from django.shortcuts import render

from LoginSignup.forms import UserProfileForm
from .forms import UserForm
from .forms import UserProfileForm
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


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

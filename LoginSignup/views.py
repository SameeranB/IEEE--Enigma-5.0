from django.shortcuts import render
from .forms import UserForm
from .forms import UserProfileForm
# Create your views here.


def IndexView(request):
    return render(request,'index.html')


def SignupView(request):

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

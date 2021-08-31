from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            user = authenticate(request,
                            username=cd['username'],
                            password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)

                    return redirect('projects')

                else:
                    return HttpResponse('Disabled Account')

            else:
                HttpResponse('Invalid Login')

    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form':form})


def signup(request):
    print(request.POST)

    print(request.user)

    # You can only run the signup script if no user is authenticated

    if request.user.is_authenticated == False:
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)

            if form.is_valid():
                new_user = form.save(commit=False)

                new_user.set_password(form.cleaned_data['password'])

                new_user.save()

                # create a profile for the user
                Profile.objects.create(
                    user=new_user
                )

                # return a seperate template if the form is validated successfully
                return render(request, 'accounts/signup_done.html', {'new_user':new_user})

        else:
            form = UserRegistrationForm()

    else:
        return redirect('logout')

    return render(request, 'accounts/signup.html', {'form':form})

# @login_required
# def profile_page(request, username):
#     profile = Profile.objects.get(user=request.user)
#
#     return render(request, 'account/profile.html', {'profile':profile})

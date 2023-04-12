from django.shortcuts import render  , redirect
from .forms import UserRegisterForm , UserProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'login to your account!!')
            return redirect('create-profile')
    else:
        form  = UserRegisterForm()
    return render(request , 'users/register.html' ,{ 'form' : form})

@login_required
def createProfile(request):
    if request.method =='POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            # form.save()
            # username = form.cleaned_data.get('username')
            # messages.success(request, f'login to your account!!')
            return redirect('dating-home')
    else:
        form  = UserProfileForm()
    return render(request , 'users/createProfile.html' ,{ 'form' : form})

from django.shortcuts import render , redirect
from .forms import UserRegisterForm , UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'create account for {username} successfuly')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html",{"form":form})


@login_required
def profile(request):
    if request.method == "POST":
        form_u = UserUpdateForm(request.POST,instance=request.user)
        form_p = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        
        if form_u.is_valid() and form_p.is_valid():
            form_u.save()
            form_p.save()
            messages.success(request,f'profile update successfuly')
            return redirect('user-profile')
        
    else:
        form_u = UserUpdateForm(instance=request.user)
        form_p = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'form_u': form_u,
        'form_p': form_p
    }

    return render(request,"users/profile.html",context)
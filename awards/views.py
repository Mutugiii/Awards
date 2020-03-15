from django.shortcuts import render, HttpResponse, loader, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Project, Rating
from .email import send_welcome_email

def signup(request):
    '''View Function for user signup'''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            email = form.cleaned_data['email']

            user = form.save()
            user.save()
            send_welcome_email(name,email)
            login(request, user)
            return redirect('create_profile')
    else:
        form = SignUpForm()
    template = loader.get_template('registration/signup.html')
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))

def logout_user(request):
    logout(request)

    return redirect(index)

def create_profile(request):
    '''View function for user to create their profile'''
    if request.method=="POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('index')
    else:
        form = ProfileForm()
    return render(request, 'registration/profile.html',{"form":form})


@login_required(login_url='/login/')
def index(request):
    '''Index View Function'''
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))
from django.shortcuts import render, HttpResponse, loader, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Project, Rating
from .email import send_welcome_email
from .forms import SignUpForm, ProfileForm, ProjectForm

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

def index(request):
    '''Index View Function'''
    template = loader.get_template('index.html')
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return HttpResponse(template.render(context, request))

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
    return render(request, 'new/profile.html',{"form":form})

def profile(request):
    '''View Function to get the users Profile'''
    profile = Profile.objects.filter(user=request.user).first()
    projects = Project.objects.filter(user=request.user).all()
    template = loader.get_template('profile.html')
    context = {
        'projects': projects,
        'profile': profile,
    }
    return HttpResponse(template.render(context, request))

def create_project(request):
    '''View Function to create a project post'''
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('index')
    else:
        form = ProjectForm()
    template = loader.get_template('new/project.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def search_project(request):
    '''View function to search for projects'''
    if 'searchprojects' in request.GET and request.GET['searchprojects']:
        search_term = request.GET.get('searchprojects')
        projects = Project.search_project(search_term)
        template = loader.get_template('search.html')
        context = {
            'projects': projects
        }
        return HttpResponse(template.render(context, request))  
    else:
        return redirect('index')
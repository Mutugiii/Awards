from django.shortcuts import render, HttpResponse, loader, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Project, Rating
from .email import send_welcome_email
from .forms import SignUpForm, ProfileForm, ProjectForm, RatingForm

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

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def search_project(request):
    '''View function to search for projects'''
    if 'searchprojects' in request.GET and request.GET['searchprojects']:
        search_term = request.GET.get('searchprojects')
        projects = Project.search_project(search_term)
        template = loader.get_template('project/search.html')
        context = {
            'projects': projects
        }
        return HttpResponse(template.render(context, request))
    else:
        return redirect('index')

@login_required(login_url='/login/')
def specificproject(request, project_id):
    '''View function to get  specific post'''
    project = Project.get_project_by_id(project_id)
    userrating = Rating.objects.filter(user = request.user).first()
    # Calculating user rating scores
    design = Rating.objects.filter(project = project.id).values_list('design', flat=True)
    usability = Rating.objects.filter(project = project.id).values_list('usability', flat=True)
    content = Rating.objects.filter(project = project.id).values_list('content', flat=True)
    design_sum = 0
    usability_sum = 0
    content_sum = 0
    for score in design:
        design_sum+=score
    for score in usability:
        usability_sum+=score
    for score in content:
        content_sum+=score
    total = int((design_sum + content_sum + usability_sum)/3)

    template = loader.get_template('project/project.html')
    context = {
        'project': project,
        'rating': total,
        'userrating': userrating,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def rate_project(request, project_id):
    '''View function to rate a project'''
    project = Project.get_project_by_id(project_id)
    if 'design' and 'usability' and 'content' in request.GET and request.GET['design']:
        rating = Rating(design = request.GET.get('design'), usability = request.GET.get('usability'), content = request.GET.get('content'))
        rating.user = request.user
        rating.project = project
        rating.status = True
        rating.save()
        return redirect('specificproject', project_id)
    else:
        return redirect('index')
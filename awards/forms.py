from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Project,Rating
from cloudinary.forms import CloudinaryFileField


class SignUpForm(UserCreationForm):
    '''Form class to sign up a user'''
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())    
    class Meta:
        model = User
        fields = ('username','email', 'password1','password2')
        

class ProfileForm(forms.ModelForm):
    '''Form class to create a new profile'''
    profile_picture = CloudinaryFileField(
        options = {
            'folder': 'awards'
       }
    )
    class Meta:
        model = Profile
        fields = ('profile_picture','profile_bio','contact_info')

class ProjectForm(forms.ModelForm):
    '''Form class to create a new post'''
    project_image = CloudinaryFileField(
        options = {
            'folder': 'awards'
        }
    )
    class Meta:
        model = Project
        fields = ('title', 'project_image', 'description', 'live_link')

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('design', 'usability', 'content')
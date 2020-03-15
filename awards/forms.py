from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Project,Rating
from cloudinary.forms import CloudinaryFileField


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())    
    class Meta:
        model = User
        fields = ('username','email', 'password1','password2')
        

class ProfileForm(forms.ModelForm):
    profile_picture = CloudinaryFileField(
        options = {
            'folder': 'awards'
       }
    )
    class Meta:
        model = Profile
        fields = ('profile_picture','profile_bio','contact_info')
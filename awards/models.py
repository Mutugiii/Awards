from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save


class CrudMethods:
    '''Method class for Common methods'''
    def save_class(self):
        '''Function to save class to database'''
        self.save()

    def delete_class(self):
        '''Function to delete class from database'''
        self.delete()

    def update_class(self, **kwargs):
        '''Function to update the class in database'''
        for key,value in kwargs.items():
            setattr(self,key,value)
            self.save()

class Project(models.Model, CrudMethods):
    '''Model class for Projects tha user posts'''
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='awardproject')
    title = models.CharField(max_length=50)
    project_image = CloudinaryField('avatar')
    description = models.TextField()
    live_link = models.CharField(max_length=100)
    published = models.DateTimeField(auto_now_add=True)


    @classmethod
    def get_project_by_id(cls, post_id):
        '''Classmethod to get a post by the given id'''
        project = Post.objects.filter(id = post_id).first()
        return project

    @classmethod
    def search_project(cls, search_term):
        '''Search for a  project by a search term'''
        projects = cls.objects.filter(title__icontains = search_term)
        return projects

    def __str__(self):
        return '{} project {}'.format(self.user.username, self.title)

class Profile(models.Model, CrudMethods):
    '''Model class for User profile'''
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='awardprofile')
    profile_picture = CloudinaryField('image')
    profile_bio = models.TextField()
    contact_info = models.EmailField()
    joined = models.DateTimeField(auto_now_add=True)
    projects = models.ForeignKey(Project, on_delete=models.CASCADE)

    @classmethod
    def get_profile_by_id(cls, profile_id):
        '''Classmethod to get a user by the profile id'''
        profile = Profile.objects.filter(id = profile_id).first()
        return profile
        
    def __str__(self):
        return self.user.username

class Rating(models.Model, CrudMethods):
    '''Model class for rating values'''
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='awardrating')
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='awardprojectrating')
    design = models.IntegerField()
    usability = models.IntegerField()
    content = models.IntegerField()

    def __str__(self):
        return self.user.design
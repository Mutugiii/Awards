from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save

class Projects(models.Model):
    '''Model class for Projects tha user posts'''
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='project')
    title = models.CharField(max_length=50)
    project_image = CloudinaryField('image')
    description = models.TextField()
    live_link = models.CharField(max_length=100)

    def __str__(self):
        return '{} project {}'.format(self.user.username, self.title)

class Profile(models.Model):
    '''Model class for User profile'''
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = CloudinaryField('image')
    profile_bio = models.TextField()
    contact_info = models.EmailField()
    projects = models.ForeignKey(Projects, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
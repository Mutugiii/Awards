from django.test import TestCase
from .models import Project,Profile,Rating
from django.contrib.auth.models import User

class TestProject(TestCase):
    '''
    Test Class for Project Model
    '''
    def setUp(self) -> None:
        '''Set up before every Testcase'''
        self.test_user = User(username='random',email='random@random.com', password='test2020')
        self.test_user.save()
        self.test_project = Project(user=self.test_user, title='Draaaake????', project_image='https://res.cloudinary.com/mutugiii/image/upload/v1583825081/gpnb9j7zld5isfk9s4he.jpg', description='Who is Draaaake????', live_link='https://github.com/Mutugiii/')

    def tearDown(self) -> None:
        '''To clean up after every test case'''
        Project.objects.all().delete()

    def test_isinstance(self):
        '''To test if object is an instance of Class'''
        self.assertTrue(isinstance(self.test_project, Project))
        
    def test_save_project(self):
        '''To test saving a project'''
        self.test_project.save_class()
        projects = Project.objects.all()
        self.assertTrue(len(projects) == 1)
    
    def test_search_project(self):
        '''To test searching for a project'''
        self.test_project.save_class()
        projects = Project.search_project('Dra')
        self.assertTrue(len(projects) == 1)

    def test_get_project_id(self):
        '''Test to get a project by Id'''
        self.test_project.save_class()
        project = Project.get_project_by_id(self.test_project.id)
        self.assertEqual(self.test_project.title, project.title)
        
    def test_update_project(self):
        '''To test updating an object'''
        self.test_project.save_class()
        self.test_project.update_class(title = 'What')
        self.assertEqual(self.test_project.title, 'What')

class TestProfile(TestCase):
    def setUp(self) -> None:
        '''Set up before every Testcase'''
        self.test_user = User(username='random',email='random@random.com', password='test2020')
        self.test_user.save()
        self.test_profile = Profile(profile_picture='https://res.cloudinary.com/mutugiii/image/upload/v1583825081/gpnb9j7zld5isfk9s4he.jpg',user=self.test_user, profile_bio='Draaaake????',contact_info='test@test.com')
        
    def tearDown(self) -> None:
        '''To clean up after running every testcase'''
        Profile.objects.all().delete()

    def test_isinstance(self):
        '''To test if object is an instance of Class'''
        self.assertTrue(isinstance(self.test_profile, Profile))

    def test_save_profile(self):
        '''Testing saving the Profile'''
        self.test_profile.save_class()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
            
    def test_update_profile_bio(self):
        '''Test updating a profile'''
        self.test_profile.save_class()
        self.test_profile.get_profile_by_id(self.test_profile.id)
        self.test_profile.update_class(profile_bio = 'This is an updated profile_bio')
        self.assertTrue(self.test_profile.profile_bio, 'This is an updated profile_bio')
        
    def test_get_profile_id(self):
        '''Test getting a profile by its Id'''
        self.test_profile.save_class()
        profile = Profile.get_profile_by_id(self.test_profile.id)
        self.assertEqual(self.test_profile.contact_info, profile.contact_info)        

class TestRating(TestCase):
    def setUp(self):
        '''Prepare for every test case'''
        self.test_user = User(username='random',email='random@random.com', password='test2020')
        self.test_user.save()
        self.test_project = Project(user=self.test_user, title='Draaaake????', project_image='https://res.cloudinary.com/mutugiii/image/upload/v1583825081/gpnb9j7zld5isfk9s4he.jpg', description='Who is Draaaake????', live_link='https://github.com/Mutugiii/')
        self.test_project.save_class()
        self.test_rating = Rating(design='1',usability='7',content='6',user=self.test_user,project=self.test_project)

    def tearDown(self) -> None:
        '''To clean up after running every testcase'''
        Rating.objects.all().delete()

    def test_isinstance(self):
        '''To test if object is an instance of Class'''
        self.assertTrue(isinstance(self.test_rating, Rating))
        
    def test_save_rating(self):
        '''Test the saving of a rating'''
        self.test_rating.save_class()
        ratings = Rating.objects.all()
        self.assertTrue(len(ratings) > 0)

        
        
        
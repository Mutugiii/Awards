from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/create/', views.create_profile, name='create_profile'),
    path('profile/user/', views.profile, name='profile'),
    path('project/create/', views.create_project, name='create_project'),
]
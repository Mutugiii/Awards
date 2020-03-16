from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/create/', views.create_profile, name='create_profile'),
    path('profile/user/', views.profile, name='profile'),
    path('project/create/', views.create_project, name='create_project'),
    path('project/search', views.search_project, name='search'),
    path('project/<int:project_id>', views.specificproject, name='specificproject'),
    path('project/rate/<int:project_id>', views.rate_project, name='rate'),
    path('award/api/profile', views.ProfileList.as_view(), name='awardapiprofile'),
    path('award/api/project', views.ProjectList.as_view(), name='awardapiproject'),
    path('award/api/tokenauth', obtain_auth_token),
    path('award/api/specific/project', views.ProjectDescription.as_view(), name='awardapispecificproject'),
]
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import *

urlpatterns = [
    path('tokenauth/',obtain_jwt_token),
    path('currentuser/', get_current_user),
    path('register/', RegisterUser.as_view()),
    path('projects/', ProjectsListCreateView.as_view(), name='projects'),
    path('project/<int:pk>', ProjectsDetailView.as_view(), name='specificproject'),
    path('profiles/', UserProfileListCreateView.as_view(), name='profiles'),
    path('profile/<int:pk>', UserProfileDetailView.as_view(), name='userprofile'),
]
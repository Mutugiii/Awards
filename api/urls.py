from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import *

urlpatterns = [
    path('currentuser/', get_current_user),
    path('login/',obtain_jwt_token),
    path('register/', RegisterUser.as_view()),
    path('projects/', ProjectsListView.as_view(), name='apiprojects'),
    path('project/<int:id>', ProjectsDetailView.as_view(), name='specificapiproject'),
    path('profile/', ProfileListView.as_view(), name='createapiprofile'),
    path('profile/<int:id>', ProfileDetailView.as_view(), name='specificapiprofle'),
    path('search/<str:search_term>', SearchProfileListView.as_view(), name='searchapiprojects'),
    path('projects/ratings/<int:id>', RatingListView.as_view(), name='apiProjectRatings'),
]
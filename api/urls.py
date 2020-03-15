from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import *

urlpatterns = [
    path('tokenauth/',obtain_jwt_token),
    path('currentuser/', get_current_user),
    path('register/', CreateUser.as_view()),
]
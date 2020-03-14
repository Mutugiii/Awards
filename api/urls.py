from django.urls import path
from .views import *

urlpatterns = [
    path('currentuser', get_current_user),
    path('users/register', CreateUser.as_view()),
]
from .serializers import GetUserSerializer, PostUserSerializer, UserProfileSerializer, UserProjectSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated
from .models import Profile, Project
from .permissions import IsOwnerProfileOrReadOnly
from django.shortcuts import Http404

@api_view(['GET'])
def get_current_user(request):
    '''Endpoint to Authenticate & fetch user information'''
    serializers = GetUserSerializer(request.user)
    return Response(serializers.data)

class RegisterUser(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self,request):
        '''Registering a user'''
        user = request.data.get('user')
        if not user:
            return Response({'response' : 'error', 'message' : 'No data found'})
        serializers = PostUserSerializer(data=user)
        if serializers.is_valid():
            saved_user = serializers.save()
        else:
            return Response({'response':'error', 'message': serializers.errors})
        return Response({'response':'success','message':'User Created Successfully'})

class ProjectsListView(APIView):
    '''View to get all the Projects and create a new Project'''
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = UserProjectSerializer(all_projects, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serialiazers = UserProjectSerializer(data=request.data)
        if serialiazers.is_valid():
            serialiazers.save()
            return Response(serialiazers.data, status=status.HTTP_201_CREATED)
        return Response(serialiazers.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectsDetailView(APIView):
    '''View all the details of a project'''
    permission_classes = [IsAuthenticated]

    def get_project(self, id):
        try:
            return Project.objects.get(pk=id)
        except Project.DoesNotExist:
            return Http404

    def get(self, request, id, format=None):
        project = get_project(id)
        serializers = UserProjectSerializer(project)
        return Response(serializers.data)

    def put(self, request, id, format=None):
        project = get_project(id)
        serializers = UserProfileSerializer(project, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        project = get_project(id)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProfileListView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        '''Function to add to a profile'''
        serializers = UserProfileSerializer(data=request.data)        
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileDetailView(APIView):
    '''View function for the user profile'''
    permission_classes = [IsOwnerProfileOrReadOnly,IsAuthenticated]
    def get_profile(self, id):
        try:
            return Profile.objects.get(pk=id)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, id, format=None):
        profile = self.get_profile(id)
        serializers = UserProfileSerializer(profile)
        return Response(serializers.data)

    def put(self, request, id, format=None):
        profile = self.get_profile(id)
        serializers = UserProfileSerializer(profile, request.data)
        if serializers.is_valid():
            serializers.save()            
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class SearchProfileListView(APIView):
    pass
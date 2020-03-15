from .serializers import GetUserSerializer, PostUserSerializer, UserProfileSerializer, UserProjectSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Profile, Project

@api_view(['GET'])
def get_current_user(request):
    '''Endpoint to Authenticate & fetch user information'''
    serializer = GetUserSerializer(request.user)
    return Response(serializer.data)

class RegisterUser(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self,request):
        '''Registering a user'''
        user = request.data.get('user')
        if not user:
            return Response({'response' : 'error', 'message' : 'No data found'})
        serializer = PostUserSerializer(data=user)
        if serializer.is_valid():
            saved_user = serializer.save()
        else:
            return Response({'response':'error', 'message': serializer.errors})
        return Response({'response':'success','message':'User Created Successfully'})

class UserProfileListCreateView(ListCreateAPIView):
    '''View to get all the profiles and create a new profile'''
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        '''Populate read-only user with the request.user'''
        user = self.request.user
        serializer.save(user=user)

class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    '''View details of a users specific profile'''
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerProfileOrReadOnly,IsAuthenticated]

class ProjectsListCreateView(ListCreateAPIView):
    '''View to get all the Projects and create a new Project'''
    queryset = Project.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        '''Populate read-only user with the request.user'''
        user = self.request.user
        serializer.save(user=user)

class ProjectsDetailView(RetrieveUpdateDestroyAPIView):
    '''View all the details of a project'''
    queryset = Project.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerProfileOrReadOnly,IsAuthenticated]
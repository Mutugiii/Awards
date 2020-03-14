from .serializers import GetUserSerializer, PostUserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import permissions

@api_view(['GET'])
def get_current_user(request):
    '''Endpoint to Authenticate & fetch user information'''
    serializer = GetUserSerializer(request.user)
    return Response(serializer.data)

class CreateUser(APIView):
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
        return Response('response':'success','message':'User Created Successfully')
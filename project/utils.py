from api.serializers import GetUserSerializer

def custom_jwt_response_handler(token,user=None,request=None):
    '''To return both user details and token for login'''
    return {
        'token': token,
        'user': GetUserSerializer(user, context={'request':request}).data
    }
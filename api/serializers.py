from rest_framework import serializers
from rest_framework.settings import api_settings
from django.contrib.auth.models import User

class GetUserSerializer(serializers.ModelSerializer):
    '''Serializer for handling GET request when user is logging in'''
    class Meta:
        model = User
        fields = ('id', 'username', 'is_superuser', 'first_name', 'last_name')

class PostUserSerializer(serializers.ModelSerializer):
    '''Serializer for handling POST requests when registering a new user'''

    # Handling conversions & Validating the input values
    # Custom token for every time user requests login
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    def get_token(self,object):
        '''
        Encodes the user information into the corresponding jwt token 
        '''
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(object)
        token = jwt_encode_handler(payload)

        return token

    def create(self,validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('token', 'username', 'password', 'first_name', 'last_name')
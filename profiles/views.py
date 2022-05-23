from bson.objectid import ObjectId
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from .serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, CreateAPIView,RetrieveUpdateAPIView
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string
# from rest_framework_social_oauth2.authentication import SocialAuthentication
from django.core.files.storage import FileSystemStorage
from django.core.files import File as FileClass
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        # print(self)
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['username'] = self.user.username
        data['email'] = self.user.email
        return data

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserRegistrationView(CreateAPIView):
    
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()   
            status_code = status.HTTP_201_CREATED
            response = {
                'success' : 'True',
                'status code' : status_code,
                'message': 'User registered successfully',
                }
            return Response(response, status=status_code)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

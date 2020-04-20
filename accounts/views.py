from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from rest_framework.views import APIView
from .models import User
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from . import views
from django.contrib.auth import logout
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from rest_framework.authtoken.views import ObtainAuthToken


from django.http import JsonResponse
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from requests.exceptions import HTTPError

from social_django.utils import load_strategy, load_backend
from social_core.backends.oauth import BaseOAuth2
from social_core.exceptions import MissingBackend, AuthTokenError, AuthForbidden
from . import serializers


def get_user(user):
    return User.objects.get(username=user)


def get_user_byid(id):
    return User.objects.get(pk=id)


def get_token(user):
    set_user = get_user(user)
    return Token.objects.get(user=set_user)


def get_groups():
    groups = []
    for g in Group.objects.all():
        groups.append(g.name)
        return groups


class SignUpView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        request.data['username'] = request.data['email']
        serializer = UserSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            print('201')
            serializer.save()
            return Response({
                status.HTTP_201_CREATED
            })
        else:
            print('400')
            return Response({
                status.HTTP_400_BAD_REQUEST
            })


class LogInView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        print('Antes de validar')
        serializer.is_valid(raise_exception=True)
        print('Despues de validar')
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'id': user.pk,
            'email': user.email,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name
        })


class LogOutView(views.APIView):
    def post(self, *args, **kwargs):
        logout(self.request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserData(views.APIView):
    def get(self, request):
        token = request.headers['Authorization'].split(' ')[1]
        user = Token.objects.get(key=token).user
        return Response({
            'id': user.pk,
            'email': user.email,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'photo': user.photo.url
            })

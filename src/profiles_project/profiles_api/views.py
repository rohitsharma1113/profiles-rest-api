from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import filters
from . import serializers
from . import models
from . import permissions

class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        sample_list = [
            'Hey',
            'Hi',
            'Hoda'
        ]

        return Response({'message':'success', 'data':sample_list})

    def post(self, request):
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data['name']
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        return Response({'method':'put'})

    def patch(self, request, pk=None):
        return Response({'method':'patch'})

    def delete(self, request, pk=None):
        return Response({'method':'delete'})



class HelloViewSet(viewsets.ViewSet):
    def list(self, request):
        sample_list = [
            'Hi',
            'Hello',
            'Nopes'
        ]
        return Response({'message':'ok', 'data':sample_list})

    def create(self, request, pk=None):
        return Response({'method':'create'})

    def retrieve(self, request, pk=None):
        return Response({'method':'retireve'})

    def update(self, request, pk=None):
        return Response({'method':'update'})

    def partial_update(self, request, pk=None):
        return Response({'method':'partial_update'})

    def destroy(self, request, pk=None):
        return Response({'method':'destroy'})


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UserProfilePermission,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self, request):
        return ObtainAuthToken().post(request)

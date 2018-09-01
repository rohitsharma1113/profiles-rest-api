from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        sample_list = [
            'Hey',
            'Hi',
            'Hoda'
        ]

        return Response({'message':'success', 'data':sample_list})

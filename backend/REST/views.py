import re
from django.shortcuts import render
from rest_framework.settings import import_from_string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import status

# Create your views here.
class testView(APIView):
    def get(self, request):
        return Response("just a test")

    def post(self, request):
        return  Response("post request")

class registerView(APIView):
    def post(self, request):    
        print(request.data)
        
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "registation sucessfull"}, status=status.HTTP_201_CREATED)
        return Response({"message" : "registration not sucessfull"}, status=status.HTTP_400_BAD_REQUEST)

class addPlaylist(APIView):
    def post(self, request):
        print(request.data)
        print(request.data['PlaylistTitle'])
        return Response({"message" : "not able to add the playlist"}, status=status.HTTP_400_BAD_REQUEST)
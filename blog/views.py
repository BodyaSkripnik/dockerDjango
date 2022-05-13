from django.shortcuts import render
from rest_framework import generics,status,permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from blog import serializers
from blog.models import films,actors,category
from blog.serializers import ActorsSerializer,CategorySerializer
from django.http import HttpResponse

class filmsList(generics.ListCreateAPIView):
    queryset = films.objects.all()
    serializer_class = serializers.FilmsSerializer
class filmsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = films.objects.all()
    serializer_class = serializers.FilmsSerializer


class actorstList(generics.ListCreateAPIView):
    queryset = actors.objects.all()
    serializer_class = serializers.ActorsSerializer
class actorsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = actors.objects.all()
    serializer_class = serializers.ActorsSerializer

class categorytList(generics.ListCreateAPIView):
    queryset = category.objects.all()
    serializer_class = serializers.CategorySerializer
class categoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = category.objects.all()
    serializer_class = serializers.CategorySerializer

def firstlist(request):
    return HttpResponse("Hello, World!")
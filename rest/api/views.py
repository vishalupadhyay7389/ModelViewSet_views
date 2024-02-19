from django.shortcuts import render
from .models import Student , StudentSerlizer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
class StudentDetailView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerlizer

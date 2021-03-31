from rest_framework import generics
from django.shortcuts import render
from .forms import SignupCreateForm
from rest_framework import viewsets

from .models import Course, Details
from rest_framework.pagination import PageNumberPagination

from.serializers import DetailsSerializer, DetailsPrLangSerializer, NewCourseSerializer


class MyPaginationClass(PageNumberPagination):
    page_size = 2


class PrLangViewset(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = DetailsPrLangSerializer
    pagination_class = MyPaginationClass


class NewCourseViewset(viewsets.ModelViewSet):
    queryset = Details.objects.all()
    serializer_class = NewCourseSerializer
    pagination_class = MyPaginationClass







# from django.shortcuts import render
# from rest_framework import viewsets
#
# from rest_framework.pagination import PageNumberPagination
#
#
# from course.models import Course, Details
# from course.serializers import DetailsPrLangSerializer, NewCourseSerializer
#
#
# class MyPaginationClass(PageNumberPagination):
#     page_size = 2
#
#
# class PrLangViewset(viewsets.ModelViewSet):
#     queryset = Course.objects.all()
#     serializer_class = DetailsPrLangSerializer
#     pagination_class = MyPaginationClass
#
#
# class NewCourseViewset(viewsets.ModelViewSet):
#     queryset = Details.objects.all()
#     serializer_class = NewCourseSerializer
#     pagination_class = MyPaginationClass

from rest_framework import generics
from django.shortcuts import render
from .forms import SignupCreateForm
from rest_framework import viewsets

from .models import Course, Details
from rest_framework.pagination import PageNumberPagination

from.serializers import DetailsSerializer, DetailsPrLangSerializer, NewCourseSerializer


class MyPaginationClass(PageNumberPagination):
    page_size = 2


# class ListApiCourse(generics.ListAPIView):
#     queryset = Details.objects.all()
#     serializer_class = DetailsSerializer
#     pagination_class = MyPaginationClass
#
#
# class DetailCourses(generics.ListAPIView):
#     queryset = Course.objects.all()
#     serializer_class = DetailsPrLangSerializer
#     pagination_class = MyPaginationClass
#
#
# class NewCourse(generics.ListAPIView):
#     queryset = Details.objects.all()
#     serializer_class = NewCourseSerializer
#     pagination_class = MyPaginationClass
#
#
# class EnrollmentCreate(generics.ListAPIView):
#     def enrollment_create(request):
#         if request.method == 'POST':
#             form = SignupCreateForm(request.POST)
#             if form.is_valid():
#                 enrollment = form.save()
#                 return render(request, 'enrollments/enrollment/created.html', {'enrollment': enrollment})
#             else:
#                 form = SignupCreateForm()


class PrLangViewset(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = DetailsPrLangSerializer
    pagination_class = MyPaginationClass


class NewCourseViewset(viewsets.ModelViewSet):
    queryset = Details.objects.all()
    serializer_class = NewCourseSerializer
    pagination_class = MyPaginationClass







from django.urls import path
from django.urls import include

from rest_framework import routers
#
from course.views import PrLangViewset, NewCourseViewset

router = routers.DefaultRouter()
router.register('prlan', PrLangViewset, basename='prlan')
router.register('newcourse', NewCourseViewset, basename='newcourse')

urlpatterns = [
    path('', include(router.urls))
]


# urlpatterns = [
#     path('<int:pk>/', PrLangViewset.as_view()),
#     path('', NewCourseViewset.as_view()),
#     # path('create/', views.EnrollmentCreate, name='enrollment_create'),
# ]

# from .views import ListApiCourse, DetailCourses, NewCourse
#
# urlpatterns = [
#     path('<int:pk>/', DetailCourses.as_view()),
#     path('', ListApiCourse.as_view()),
#     path('', NewCourse.as_view())
# ]
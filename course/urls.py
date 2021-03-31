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



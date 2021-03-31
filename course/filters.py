from django_filters import rest_framework as filters

from .models import Course


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class CourseFilter(filters.FilterSet):

    class Meta:
        model = Course
        fields = ['id', 'title']
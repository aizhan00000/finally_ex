from rest_framework import serializers
from .models import Course, Details


class DetailsSerializer(serializers.ModelSerializer):
    totally = serializers.SerializerMethodField()

    class Meta:
        model = Details
        fields = ['id', 'title', 'pr_languages', 'totally', 'per_month', 'duration']

    def get_totally(self, instance):
        return instance.per_month * instance.duration


class DetailsPrLangSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'title', 'address']


class NewCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = ['id', 'title', 'pr_languages', 'duration', 'price_per_month']

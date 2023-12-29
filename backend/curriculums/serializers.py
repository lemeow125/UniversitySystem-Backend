from rest_framework import serializers
from courses.models import Course


class CurriculumSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=64)

    class Meta:
        model = Course
        fields = ['id', 'name', 'timestamp']
        read_only_fields = ['id', 'timestamp']

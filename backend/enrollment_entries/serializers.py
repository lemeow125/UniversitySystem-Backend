from rest_framework import serializers
from courses.models import Course
from users.models import CustomUser
from enrollment_entries.models import EnrollmentEntry


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'name', 'code', 'curriculum']


class CustomUserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='full_name')

    class Meta:
        model = CustomUser
        fields = ['id', 'name']


class EnrollmentEntrySerializer(serializers.ModelSerializer):
    student = serializers.SlugRelatedField(
        many=False, slug_field='id', queryset=CustomUser.objects.all(), required=True, allow_null=False)
    course = serializers.SlugRelatedField(
        many=False, slug_field='id', queryset=Course.objects.all(), required=True, allow_null=False)

    class Meta:
        model = EnrollmentEntry
        fields = ['id', 'student', 'course', 'timestamp']
        read_only_fields = ['id', 'timestamp']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['student'] = CustomUserSerializer(instance.student).data
        rep['course'] = CourseSerializer(instance.course).data
        return rep

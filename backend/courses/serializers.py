from rest_framework import serializers
from courses.models import Course
from curriculums.models import Curriculum


class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name']


class CourseSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=64)
    code = serializers.CharField(max_length=32)
    curriculum = serializers.SlugRelatedField(
        many=False, slug_field='id', queryset=Curriculum.objects.all(), required=True, allow_null=False)

    class Meta:
        model = Course
        fields = ['id', 'name', 'code', 'curriculum', 'timestamp']
        read_only_fields = ['id', 'timestamp']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['curriculum'] = CurriculumSerializer(instance.curriculum).data
        return rep

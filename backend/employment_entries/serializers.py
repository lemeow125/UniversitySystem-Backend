from rest_framework import serializers
from departments.models import Department
from users.models import CustomUser
from employment_entries.models import EmploymentEntry


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ['id', 'name']


class CustomUserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='full_name')

    class Meta:
        model = CustomUser
        fields = ['id', 'name']


class EmploymentEntrySerializer(serializers.ModelSerializer):
    employee = serializers.SlugRelatedField(
        many=False, slug_field='id', queryset=CustomUser.objects.all(), required=True, allow_null=False)
    department = serializers.SlugRelatedField(
        many=False, slug_field='id', queryset=Department.objects.all(), required=True, allow_null=False)

    class Meta:
        model = EmploymentEntry
        fields = ['id', 'employee', 'department', 'salary', 'timestamp']
        read_only_fields = ['id', 'timestamp']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['employee'] = CustomUserSerializer(instance.employee).data
        rep['department'] = DepartmentSerializer(instance.department).data
        return rep

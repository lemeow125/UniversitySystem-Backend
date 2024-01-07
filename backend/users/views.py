from users.models import CustomUser
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from users.serializers import CustomUserSerializer
from django.core.cache import cache


class TeacherViewSet(generics.ListAPIView):
    # Returns list of users who are teachers
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        key = 'teachers'
        queryset = cache.get(key)
        if not queryset:
            queryset = CustomUser.objects.filter(is_teacher=True)
            cache.set(key, queryset, 60*60)  # Cache for an hour
        return queryset


class StudentViewSet(generics.ListAPIView):
    # Returns list of users who are students
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        key = 'students'
        queryset = cache.get(key)
        if not queryset:
            queryset = CustomUser.objects.filter(is_student=True)
            cache.set(key, queryset, 60*60)  # Cache for an hour
        return queryset


class EmployeeViewSet(generics.ListAPIView):
    # Returns list of users who are employees
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        key = 'employees'
        queryset = cache.get(key)
        if not queryset:
            queryset = CustomUser.objects.filter(is_employee=True)
            cache.set(key, queryset, 60*60)  # Cache for an hour
        return queryset

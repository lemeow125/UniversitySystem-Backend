from users.models import CustomUser
from users.permissions import IsStudent
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from users.serializers import CustomUserSerializer
from rest_framework.response import Response


class TeacherViewSet(generics.ListAPIView):
    # Returns list of users who are teachers
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(is_teacher=True)


class StudentViewSet(generics.ListAPIView):
    # Returns list of users who are students
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(is_student=True)


class EmployeeViewSet(generics.ListAPIView):
    # Returns list of users who are employees
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(is_employee=True)

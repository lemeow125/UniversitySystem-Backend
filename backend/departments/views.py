from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from departments.models import Department
from departments.serializers import DepartmentSerializer


class DepartmentViewSet(generics.ListAPIView):
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        return Department.objects.all()

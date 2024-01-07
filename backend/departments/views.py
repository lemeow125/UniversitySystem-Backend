from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from departments.models import Department
from departments.serializers import DepartmentSerializer
from django.core.cache import cache


class DepartmentViewSet(generics.ListAPIView):
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        key = 'departments'
        queryset = cache.get(key)
        if not queryset:
            queryset = Department.objects.all()
            cache.set(key, queryset, 60*60)  # Cache for an hour
        return queryset

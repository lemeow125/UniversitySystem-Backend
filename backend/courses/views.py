from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from courses.serializers import CourseSerializer
from courses.models import Course
from django.core.cache import cache


class CourseViewSet(generics.ListAPIView):
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]
    serializer_class = CourseSerializer

    def get_queryset(self):
        key = 'courses'
        queryset = cache.get(key)
        if not queryset:
            queryset = Course.objects.all()
            cache.set(key, queryset, 60*60)  # Cache for an hour
        return queryset

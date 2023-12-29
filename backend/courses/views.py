from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from courses.serializers import CourseSerializer
from courses.models import Course


class CourseViewSet(generics.ListAPIView):
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]
    serializer_class = CourseSerializer

    def get_queryset(self):
        return Course.objects.all()

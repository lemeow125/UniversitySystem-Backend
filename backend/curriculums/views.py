from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from curriculums.serializers import CurriculumSerializer
from curriculums.models import Curriculum
from django.core.cache import cache


class CurriculumViewSet(generics.ListAPIView):
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]
    serializer_class = CurriculumSerializer

    def get_queryset(self):
        key = 'curriculums'
        queryset = cache.get(key)
        if not queryset:
            queryset = Curriculum.objects.all()
            cache.set(key, queryset, 60*60)  # Cache for an hour
        return queryset

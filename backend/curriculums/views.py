from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from curriculums.serializers import CurriculumSerializer
from curriculums.models import Curriculum


class CurriculumViewSet(generics.ListAPIView):
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]
    serializer_class = CurriculumSerializer

    def get_queryset(self):
        return Curriculum.objects.all()

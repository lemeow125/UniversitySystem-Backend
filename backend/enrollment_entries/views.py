from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from enrollment_entries.serializers import EnrollmentEntrySerializer
from enrollment_entries.models import EnrollmentEntry


class EnrollmentViewSet(generics.ListAPIView):
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]
    serializer_class = EnrollmentEntrySerializer

    def get_queryset(self):
        return EnrollmentEntry.objects.all()


class SelfEnrollmentViewSet(generics.ListAPIView):
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]
    serializer_class = EnrollmentEntrySerializer

    def get_queryset(self):
        user = self.kwargs['id']
        return EnrollmentEntry.objects.filter(student=user)

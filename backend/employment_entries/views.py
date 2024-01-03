from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, viewsets
from employment_entries.serializers import EmploymentEntrySerializer
from employment_entries.models import EmploymentEntry
from users.permissions import IsHiringStaffOrReadOnly


class EmploymentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsHiringStaffOrReadOnly]
    serializer_class = EmploymentEntrySerializer

    def get_queryset(self):
        return EmploymentEntry.objects.all()


class SelfEmploymentViewSet(generics.ListAPIView):
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]
    serializer_class = EmploymentEntrySerializer

    def get_queryset(self):
        user = self.kwargs['id']
        return EmploymentEntry.objects.filter(employee=user)

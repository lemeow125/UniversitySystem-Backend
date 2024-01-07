from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, viewsets
from employment_entries.serializers import EmploymentEntrySerializer
from employment_entries.models import EmploymentEntry
from users.permissions import IsHiringStaffOrReadOnly
from django.core.cache import cache


class EmploymentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsHiringStaffOrReadOnly]
    serializer_class = EmploymentEntrySerializer

    def get_queryset(self):
        key = 'employment_entries'
        queryset = cache.get(key)
        if not queryset:
            queryset = EmploymentEntry.objects.all()
            cache.set(key, queryset, 60*60)  # Cache for an hour
        return queryset


class SelfEmploymentViewSet(generics.ListAPIView):
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]
    serializer_class = EmploymentEntrySerializer

    def get_queryset(self):
        user = self.request.user
        key = ('employment_entry:'+str(user.id))
        queryset = cache.get(key)
        if not queryset:
            queryset = EmploymentEntry.objects.filter(employee=user.id)
            cache.set(key, queryset, 60*60)  # Cache for an hour
        return queryset

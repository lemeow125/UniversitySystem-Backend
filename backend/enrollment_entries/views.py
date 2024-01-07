from rest_framework.permissions import IsAuthenticated
from users.permissions import IsEnrollmentStaffOrReadOnly
from rest_framework import generics, viewsets
from enrollment_entries.serializers import EnrollmentEntrySerializer
from enrollment_entries.models import EnrollmentEntry
from django.core.cache import cache


class EnrollmentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsEnrollmentStaffOrReadOnly]
    serializer_class = EnrollmentEntrySerializer

    def get_queryset(self):
        key = 'enrollment_entries'
        queryset = cache.get(key)
        if not queryset:
            queryset = EnrollmentEntry.objects.all()
            cache.set(key, queryset, 60*60)  # Cache for an hour
            print('test')
        return queryset


class SelfEnrollmentViewSet(generics.ListAPIView):
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]
    serializer_class = EnrollmentEntrySerializer

    def get_queryset(self):
        user = self.request.user
        key = ('enrollment_entry:'+str(user.id))
        queryset = cache.get(key)
        if not queryset:
            queryset = EnrollmentEntry.objects.filter(student=user.id)
            cache.set(key, queryset, 60*60)  # Cache for an hour
        return queryset

from django.urls import path, include
from django.contrib.staticfiles.views import serve
from config import settings

urlpatterns = [
    path('accounts/', include('users.urls')),
    path('curriculums/', include('curriculums.urls')),
    path('courses/', include('courses.urls')),
    path('enrollment_entries/', include('enrollment_entries.urls')),
    path('departments/', include('departments.urls')),
    path('employment_entries/', include('employment_entries.urls')),
    path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT}),
]

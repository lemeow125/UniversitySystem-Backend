from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from config import settings

urlpatterns = [
    path('accounts/', include('users.urls')),
    path('curriculums/', include('curriculums.urls')),
    path('courses/', include('courses.urls')),
    path('enrollment_entries/', include('enrollment_entries.urls')),
    path('departments/', include('departments.urls')),
    path('employment_entries/', include('employment_entries.urls')),
]

# Serving media files
# Only used in development
# Use Nginx for serving media files in production!
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        'media/', document_root=settings.MEDIA_ROOT)

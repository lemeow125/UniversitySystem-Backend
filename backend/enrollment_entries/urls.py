from django.urls import path, include
from enrollment_entries import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.EnrollmentViewSet, basename="Enrollment Entries")


urlpatterns = [
    path('', include(router.urls)),
    path('self/', views.SelfEnrollmentViewSet.as_view()),

]

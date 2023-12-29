from django.urls import path, include
from enrollment_entries import views

urlpatterns = [
    path('', views.EnrollmentViewSet.as_view()),
    path('self/', views.EnrollmentViewSet.as_view()),
]

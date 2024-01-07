from django.urls import path, include
from employment_entries import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.EmploymentViewSet, basename="Employment Entries")

urlpatterns = [
    path('self/', views.SelfEmploymentViewSet.as_view()),
    path('', include(router.urls)),
]

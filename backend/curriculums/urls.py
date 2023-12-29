from django.urls import path, include
from curriculums import views

urlpatterns = [
    path('', views.CurriculumViewSet.as_view()),
]

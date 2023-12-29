from django.urls import path, include
from courses import views

urlpatterns = [
    path('', views.CourseViewSet.as_view()),
]

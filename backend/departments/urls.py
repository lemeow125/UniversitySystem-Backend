from django.urls import path, include
from departments import views

urlpatterns = [
    path('', views.DepartmentViewSet.as_view()),
]

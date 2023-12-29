from django.urls import path, include
from users import views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('teachers/', views.TeacherViewSet.as_view()),
    path('students/', views.StudentViewSet.as_view()),
    path('employees/', views.EmployeeViewSet.as_view()),
]

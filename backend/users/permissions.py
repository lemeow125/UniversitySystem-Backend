from rest_framework.permissions import BasePermission


class IsEmployee(BasePermission):
    message = "You must be an employee to perform this action."

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_employee

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.is_employee


class IsTeacher(BasePermission):
    message = "You must be a teacher to perform this action."

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_teacher

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.is_teacher


class IsStudent(BasePermission):
    message = "You must be a student to perform this action."

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_student

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.is_student

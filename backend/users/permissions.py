from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsEmployee(BasePermission):
    message = "You must be an employee to perform this action."

    def has_permission(self, request, view):
        return request.user.employmententry_set.exists()

    def has_object_permission(self, request, view, obj):
        return request.user.employmententry_set.exists()


class IsTeacher(BasePermission):
    message = "You must be a teacher or professor to perform this action."

    def has_permission(self, request, view):
        return request.user.employmententry_set.filter(is_professor=True).exists()

    def has_object_permission(self, request, view, obj):
        return request.user.employmententry_set.filter(is_professor=True).exists()


class IsHiringStaff(BasePermission):
    message = "You must be hiring staff to perform this action."

    def has_permission(self, request, view):
        return request.user.employmententry_set.filter(is_hiring_staff=True).exists()

    def has_object_permission(self, request, view, obj):
        return request.user.employmententry_set.filter(is_hiring_staff=True).exists()


class IsHiringStaffOrReadOnly(BasePermission):
    message = "You must be hiring staff to perform this action."

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.employmententry_set.filter(
                is_enrollment_staff=True).exists()
        )


class IsEnrollmentStaff(BasePermission):
    message = "You must be a enrollment staff to perform this action."

    def has_permission(self, request, view):
        return request.user.employmententry_set.filter(is_enrollment_staff=True).exists()

    def has_object_permission(self, request, view, obj):
        return request.user.employmententry_set.filter(is_enrollment_staff=True).exists()


class IsEnrollmentStaffOrReadOnly(BasePermission):
    message = "You must be a enrollment staff to perform this action."

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.employmententry_set.filter(
                is_enrollment_staff=True).exists()
        )


class IsStudent(BasePermission):
    message = "You must be a student to perform this action."

    def has_permission(self, request, view):
        return request.user.is_student

    def has_object_permission(self, request, view, obj):
        return request.user.is_student

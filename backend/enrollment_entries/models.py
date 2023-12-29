from django.db import models
from users.models import CustomUser
from courses.models import Course
from django.utils.timezone import now


class EnrollmentEntry(models.Model):
    student = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return f"{self.student} enrolled in {self.course}"

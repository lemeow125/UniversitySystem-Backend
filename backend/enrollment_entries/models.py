from django.db import models
from users.models import CustomUser
from courses.models import Course
from curriculums.models import Curriculum
from django.utils.timezone import now
from django.db.models.signals import post_migrate
from django.dispatch import receiver


class EnrollmentEntry(models.Model):
    student = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT, related_name='enrollmententry_set')
    course = models.ForeignKey(
        Course, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return f"{self.student} enrolled in {self.course}"


@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    if sender.name == 'enrollment_entries':
        # Add test students here if needed
        # Users will automatically be enrolled created after migrating the db
        users = [
            # Debug Student
            {
                'username': 'debug-student',
                'course': 'Bachelor of Science in Information Technology',
                'curriculum': 'CITC BSIT 2018-2019'
            },
        ]

        for user in users:
            CURRICULUM = Curriculum.objects.filter(
                name=user['curriculum']).first()
            COURSE = Course.objects.filter(
                name=user['course'], curriculum=CURRICULUM).first()
            USER = CustomUser.objects.filter(
                username=user['username']).first()
            if not EnrollmentEntry.objects.filter(student=USER, course=COURSE).exists():
                ENROLLMENT_ENTRY = EnrollmentEntry.objects.create(
                    student=USER,
                    course=COURSE,
                )
                print('Enrolled User:', user['username'], 'in', user['course'])

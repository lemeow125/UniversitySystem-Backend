from django.db import models
from users.models import CustomUser
from departments.models import Department
from django.utils.timezone import now
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.cache import cache
import logging


class EmploymentEntry(models.Model):
    employee = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT, related_name='employmententry_set')
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT)
    is_professor = models.BooleanField(default=False)
    is_enrollment_staff = models.BooleanField(default=False)
    is_hiring_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=64)
    salary = models.FloatField(default=0)
    timestamp = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return f"{self.employee} employed in {self.department}"

    def save(self, *args, **kwargs):
        # Cache invalidation on changes
        cache.delete('employment_entries')
        cache.delete('employment_entry:'+str(self.employee.id))
        return super().save(*args, **kwargs)


@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    if sender.name == 'employment_entries':
        # Add test employees here if needed
        # Users will automatically be employed created after migrating the db
        employees = [
            # Debug Professor
            {
                'username': 'debug-employee-professor',
                'department': 'CITC',
                'is_professor': True,
                'is_enrollment_staff': False,
                'is_hiring_staff': False,
                'role': 'Instructor',
                'salary': 25000,
            },
            # Debug Hiring Staff
            {
                'username': 'debug-employee-hiringstaff',
                'department': 'Human Resources',
                'is_professor': False,
                'is_enrollment_staff': False,
                'is_hiring_staff': True,
                'role': 'Generic Employee',
                'salary': 23000,
            },
            # Debug Enrollment Staff
            {
                'username': 'debug-employee-enrollmentstaff',
                'department': 'Admissions',
                'is_professor': False,
                'is_enrollment_staff': True,
                'is_hiring_staff': False,
                'role': 'Generic Employee',
                'salary': 23000,
            },
        ]

        for employee in employees:
            DEPARTMENT = Department.objects.filter(
                name=employee['department']).first()
            USER = CustomUser.objects.filter(
                username=employee['username']).first()

            if not EmploymentEntry.objects.filter(employee=USER, department=DEPARTMENT).exists():
                EMPLOYMENT_ENTRY = EmploymentEntry.objects.create(
                    employee=USER,
                    department=DEPARTMENT,
                    role=employee['role'],
                    is_professor=employee['is_professor'],
                    is_enrollment_staff=employee['is_enrollment_staff'],
                    is_hiring_staff=employee['is_hiring_staff'],
                    salary=employee['salary']
                )
                print('Employed User:',
                      employee['username'], 'in', employee['department'])

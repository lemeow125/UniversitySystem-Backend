from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField
from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver
import os


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100, null=True, default=None)
    last_name = models.CharField(max_length=100, null=True, default=None)
    # email inherited from base user class
    # username inherited from base user class
    # password inherited from base user class
    # is_admin inherited from base user class
    is_banned = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    student_id = models.IntegerField(null=True, unique=True)
    contact_number = models.BigIntegerField(null=True)
    avatar = ResizedImageField(
        null=True, force_format="WEBP", quality=100, upload_to='avatars/')

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def is_employee(self):
        return self.employmententry_set.exists()

    @property
    def is_student(self):
        return self.enrollmententry_set.exists()

    @property
    def is_employee(self):
        return self.employmententry_set.exists()

    pass


@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    if sender.name == 'users':
        # Add test users here if needed
        # They will automatically be created after migrating the db
        users = [
            # Superadmin Account
            {
                'username': os.getenv('DJANGO_ADMIN_USERNAME'),
                'email': os.getenv('DJANGO_ADMIN_EMAIL'),
                'password': os.getenv('DJANGO_ADMIN_PASSWORD'),
                'is_staff': True,
                'is_superuser': True,
                'student_id': None,
                'first_name': None,
                'last_name': None
            },
            # Debug Student
            {
                'username': 'debug-student',
                'email': os.getenv('DJANGO_ADMIN_EMAIL'),
                'password': os.getenv('DJANGO_ADMIN_PASSWORD'),
                'is_staff': False,
                'is_superuser': False,
                'student_id': 1,
                'first_name': "Test",
                'last_name': "Student"
            },
            # Debug Professor
            {
                'username': 'debug-employee-professor',
                'email': os.getenv('DJANGO_ADMIN_EMAIL'),
                'password': os.getenv('DJANGO_ADMIN_PASSWORD'),
                'is_staff': False,
                'is_superuser': False,
                'student_id': None,
                'first_name': "Test",
                'last_name': "Employee"
            },
            # Debug Hiring Staff
            {
                'username': 'debug-employee-hiringstaff',
                'email': os.getenv('DJANGO_ADMIN_EMAIL'),
                'password': os.getenv('DJANGO_ADMIN_PASSWORD'),
                'is_staff': False,
                'is_superuser': False,
                'student_id': None,
                'first_name': "Test",
                'last_name': "Employee"
            },
            # Debug Enrollment Staff
            {
                'username': 'debug-employee-enrollmentstaff',
                'email': os.getenv('DJANGO_ADMIN_EMAIL'),
                'password': os.getenv('DJANGO_ADMIN_PASSWORD'),
                'is_staff': False,
                'is_superuser': False,
                'student_id': None,
                'first_name': "Test",
                'last_name': "Employee"
            },
        ]

        for user in users:
            if not CustomUser.objects.filter(username=user['username']).exists():
                if (user['is_superuser']):
                    USER = CustomUser.objects.create_superuser(
                        username=user['username'],
                        password=user['password'],
                        email=user['email'],
                    )
                    print('Created Superuser:', user['username'])
                else:
                    USER = CustomUser.objects.create_user(
                        username=user['username'],
                        password=user['password'],
                        email=user['email'],
                    )
                    print('Created User:', user['username'])
                USER.first_name = user['first_name']
                USER.last_name = user['last_name']
                USER.is_active = True
                USER.student_id = user['student_id']
                USER.save()

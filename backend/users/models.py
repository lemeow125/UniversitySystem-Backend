from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField
from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver
import os


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # email inherited from base user class
    # username inherited from base user class
    # password inherited from base user class
    # is_admin inherited from base user class
    is_banned = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    student_id = models.IntegerField(null=True, unique=True)
    contact_number = models.BigIntegerField(null=True)
    avatar = ResizedImageField(null=True, force_format="WEBP", quality=100)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
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
                'is_student': False,
                'is_teacher': False,
                'is_staff': True,
                'is_superuser': True,
                'student_id': None
            },
            # Debug Student
            {
                'username': 'debug-student',
                'email': os.getenv('DJANGO_ADMIN_EMAIL'),
                'password': os.getenv('DJANGO_ADMIN_PASSWORD'),
                'is_student': True,
                'is_teacher': False,
                'is_staff': False,
                'is_superuser': False,
                'student_id': 1
            },
        ]

        for user in users:
            if not CustomUser.objects.filter(username=user['username']).exists():
                USER = CustomUser.objects.create_user(
                    username=user['username'],
                    password=user['password'],
                    email=user['email']
                )
                USER.is_active = True
                USER.is_student = user['is_student']
                USER.is_staff = user['is_staff']
                USER.is_superuser = user['is_superuser']
                USER.student_id = user['student_id']
                USER.save()
                print('Created User:', user['username'])

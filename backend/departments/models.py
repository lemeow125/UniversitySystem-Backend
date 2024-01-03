from django.db import models
from django.utils.timezone import now
from django.db.models.signals import post_migrate
from django.dispatch import receiver


class Department(models.Model):
    name = models.CharField(max_length=64)
    timestamp = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return f"{self.name}"


@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    if sender.name == 'departments':
        # Seeding the db with preset departments
        departments = [
            {
                'name': 'CITC',
            },
            {
                'name': 'Admissions',
            },
            {
                'name': 'Human Resources',
            },
        ]

        for department in departments:
            if not Department.objects.filter(name=department['name']).exists():
                DEPARTMENT = Department.objects.create(
                    name=department['name'],
                )
                print('Created Department:', department['name'])

from django.db import models
from django.utils.timezone import now
from django.db.models.signals import post_migrate
from django.dispatch import receiver


class Curriculum(models.Model):
    name = models.TextField()
    timestamp = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return f"{self.name}"


@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    if sender.name == 'curriculums':
        # Seeding the db with preset curriculums
        curriculums = [
            {
                'name': 'CITC BSIT 2018-2019',
            },
        ]

        for curriculum in curriculums:
            if not Curriculum.objects.filter(name=curriculum['name']).exists():
                COURSE = Curriculum.objects.create(
                    name=curriculum['name'],
                )
                print('Created curriculum:', curriculum['name'])

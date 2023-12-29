from django.db import models
from django.utils.timezone import now
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from curriculums.models import Curriculum


class Course(models.Model):
    name = models.TextField()
    code = models.TextField()
    curriculum = models.ForeignKey(
        Curriculum, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return f"{self.name}"


@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    if sender.name == 'courses':
        # Seeding the db with preset courses
        courses = [
            {
                'name': 'Bachelor of Science in Information Technology',
                'code': 'BSIT',
                'curriculum': 'CITC BSIT 2018-2019',
            },
        ]

        for course in courses:
            CURRICULUM = Curriculum.objects.filter(
                name=course['curriculum']).first()
            if not Course.objects.filter(name=course['name']).filter(code=course['code']).filter(curriculum=CURRICULUM).exists():
                COURSE = Course.objects.create(
                    name=course['name'],
                    code=course['code'],
                    curriculum=CURRICULUM
                )

                print('Created course:',
                      course['name'], 'under curriculum', course['curriculum'])

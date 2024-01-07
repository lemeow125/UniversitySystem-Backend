from django.db import models
from django.utils.timezone import now
from django.db.models.signals import post_migrate, post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache


class Curriculum(models.Model):
    name = models.TextField()
    timestamp = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return f"{self.name}"


def clear_cache(instance):
    # Cache invalidation on changes
    cache.delete('curriculum')


sender = Curriculum


@receiver(post_save, sender=sender)
# On model save or create
def on_update(sender, instance, **kwargs):
    clear_cache(instance)


@receiver(post_delete, sender=sender)
# On model delete
def on_delete(sender, instance, **kwargs):
    clear_cache(instance)


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
                print('Created Curriculum:', curriculum['name'])

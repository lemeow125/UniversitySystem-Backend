# Generated by Django 5.0 on 2024-01-03 14:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
    ]

# Generated by Django 5.0 on 2023-12-27 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='student_id',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
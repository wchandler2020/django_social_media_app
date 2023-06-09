# Generated by Django 4.2 on 2023-04-29 16:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5aedccb3-16f4-42d9-971c-f2f7b057d1c1'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterModelTable(
            name='project',
            table='tb_projects',
        ),
    ]

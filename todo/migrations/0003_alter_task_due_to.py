# Generated by Django 4.1.5 on 2023-04-19 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_task_task_task_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_to',
            field=models.DateField(blank=True, null=True),
        ),
    ]

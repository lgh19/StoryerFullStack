# Generated by Django 4.1.1 on 2022-10-19 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storyer', '0006_rename_group_student_assigned_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='preferences',
            field=models.ManyToManyField(related_name='group_preferences', through='storyer.Preference', to='storyer.group'),
        ),
    ]

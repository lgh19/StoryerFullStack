# Generated by Django 4.1.1 on 2022-10-19 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storyer', '0005_rename_group_preference_group_preference_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='group',
            new_name='assigned_group',
        ),
        migrations.AlterField(
            model_name='student',
            name='preferences',
            field=models.ManyToManyField(related_name='group_preference', through='storyer.Preference', to='storyer.group'),
        ),
    ]
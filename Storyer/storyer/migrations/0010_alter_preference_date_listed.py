# Generated by Django 4.1.1 on 2022-10-19 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storyer', '0009_alter_preference_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preference',
            name='date_listed',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
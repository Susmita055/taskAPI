# Generated by Django 3.2.4 on 2021-08-04 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-05 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='date',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='email',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='guest',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='message',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='time',
        ),
    ]

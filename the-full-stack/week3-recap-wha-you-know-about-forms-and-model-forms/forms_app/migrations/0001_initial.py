# Generated by Django 5.0.3 on 2024-03-07 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('worksite', models.CharField(max_length=200)),
                ('job_title', models.CharField(max_length=200)),
                ('comments', models.TextField()),
            ],
        ),
    ]

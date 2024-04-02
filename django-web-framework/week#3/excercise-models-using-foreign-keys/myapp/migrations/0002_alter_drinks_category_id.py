# Generated by Django 5.0.3 on 2024-03-31 22:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinks',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='drinks', to='myapp.drinkscategory'),
        ),
    ]

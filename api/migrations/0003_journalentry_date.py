# Generated by Django 5.1 on 2024-08-24 00:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='journalentry',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

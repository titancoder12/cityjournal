# Generated by Django 5.1 on 2024-08-18 04:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='')),
                ('entry_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.journalentry')),
            ],
        ),
    ]

# Generated by Django 3.2 on 2021-05-01 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_teambet_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teambet',
            name='datetime',
        ),
    ]

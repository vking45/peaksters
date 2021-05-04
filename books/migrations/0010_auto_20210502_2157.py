# Generated by Django 3.2 on 2021-05-02 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0009_auto_20210501_2223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='point',
            name='user',
        ),
        migrations.AddField(
            model_name='point',
            name='user_current',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_current', to=settings.AUTH_USER_MODEL),
        ),
    ]

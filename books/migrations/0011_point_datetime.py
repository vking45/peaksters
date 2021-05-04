# Generated by Django 3.2 on 2021-05-02 17:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20210502_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
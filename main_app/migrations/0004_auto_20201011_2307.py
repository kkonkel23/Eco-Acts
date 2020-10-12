# Generated by Django 3.1.2 on 2020-10-11 23:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0003_myactivity_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myactivity',
            name='about',
        ),
        migrations.RemoveField(
            model_name='myactivity',
            name='name',
        ),
        migrations.RemoveField(
            model_name='myactivity',
            name='savings',
        ),
        migrations.AddField(
            model_name='myactivity',
            name='my_activities',
            field=models.ManyToManyField(to='main_app.Activity'),
        ),
        migrations.AlterField(
            model_name='myactivity',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

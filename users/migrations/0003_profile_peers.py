# Generated by Django 3.1.5 on 2021-01-21 14:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_auto_20210121_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='peers',
            field=models.ManyToManyField(related_name='network', to=settings.AUTH_USER_MODEL),
        ),
    ]
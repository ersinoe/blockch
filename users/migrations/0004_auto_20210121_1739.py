# Generated by Django 3.1.5 on 2021-01-21 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_peers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='peers',
            field=models.ManyToManyField(related_name='_profile_peers_+', to='users.Profile'),
        ),
    ]
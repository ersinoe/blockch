# Generated by Django 3.1.5 on 2021-01-22 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210121_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='secret_passcode',
            field=models.CharField(default='', max_length=100),
        ),
    ]

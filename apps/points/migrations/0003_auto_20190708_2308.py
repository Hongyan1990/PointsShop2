# Generated by Django 2.2.2 on 2019-07-08 15:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('points', '0002_points_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='points',
            unique_together={('user', 'points_user')},
        ),
    ]

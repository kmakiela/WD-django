# Generated by Django 2.0.6 on 2018-06-13 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WD', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participantlist',
            name='mark',
        ),
    ]

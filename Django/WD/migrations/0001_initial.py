# Generated by Django 2.0.6 on 2018-06-12 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('max_participants', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(default=1)),
                ('comment', models.TextField(max_length=300)),
                ('first_try', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WD.Course')),
                ('mark', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='WD.Mark')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('birthdate', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='participantlist',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WD.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='participants',
            field=models.ManyToManyField(through='WD.ParticipantList', to='WD.Student'),
        ),
    ]
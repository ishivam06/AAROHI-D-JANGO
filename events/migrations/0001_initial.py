# Generated by Django 3.2.12 on 2022-02-07 05:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('structure', models.TextField()),
                ('rules', models.TextField(null=True)),
                ('document', models.FileField(null=True, upload_to='competition_docs')),
                ('image', models.FileField(upload_to='events')),
                ('date', models.DateField()),
                ('platform', models.CharField(max_length=40)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('fees', models.IntegerField()),
                ('reg_link_solo', models.CharField(max_length=200, null=True)),
                ('reg_link_duo', models.CharField(max_length=200, null=True)),
                ('reg_link_group', models.CharField(max_length=200, null=True)),
                ('last_registration_date', models.DateField()),
                ('managers', models.ManyToManyField(to='accounts.Manager')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_participants', models.IntegerField()),
                ('date_of_reg', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('participants', models.ManyToManyField(to='accounts.Participant')),
            ],
        ),
    ]

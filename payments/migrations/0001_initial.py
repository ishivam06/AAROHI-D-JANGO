# Generated by Django 3.2.12 on 2022-02-08 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0002_auto_20220207_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=13)),
                ('amount', models.IntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='events.event')),
            ],
        ),
    ]
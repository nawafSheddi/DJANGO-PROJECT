# Generated by Django 3.2.14 on 2022-08-03 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gatheringApp', '0004_alter_gather_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='gather',
            name='leaderPhoneNumber',
            field=models.CharField(default=-1, max_length=12),
            preserve_default=False,
        ),
    ]

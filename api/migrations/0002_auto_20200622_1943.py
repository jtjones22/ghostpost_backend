# Generated by Django 3.0.7 on 2020-06-22 19:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postitem',
            name='vote_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='postitem',
            name='magic_key',
            field=models.CharField(default='sMmdgn', editable=False, max_length=6),
        ),
        migrations.AlterField(
            model_name='postitem',
            name='submission_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, editable=False),
        ),
    ]

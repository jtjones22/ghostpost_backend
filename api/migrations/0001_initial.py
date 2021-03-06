# Generated by Django 3.0.7 on 2020-06-22 19:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_choice', models.CharField(choices=[('roast', 'ROAST'), ('boast', 'BOAST')], max_length=50)),
                ('text', models.CharField(max_length=280)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('submission_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('magic_key', models.CharField(default='pNqXAG', editable=False, max_length=6)),
            ],
        ),
    ]

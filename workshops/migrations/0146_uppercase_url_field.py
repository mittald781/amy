# Generated by Django 2.0.7 on 2018-07-23 19:06

import re

import django
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0145_profileupdaterequest_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingprogress',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='task',
            name='url',
            field=models.URLField(blank=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='event',
            name='url',
            field=models.CharField(blank=True, help_text='Required in order for this event to be "published".<br />Use link to the event\'s <b>website</b>, not repository.', max_length=100, null=True, unique=True, validators=[django.core.validators.RegexValidator(re.compile('https?://github\\.com/(?P<name>[^/]+)/(?P<repo>[^/]+)/?'), inverse_match=True)], verbose_name='URL'),
        ),
    ]

# Generated by Django 2.1.7 on 2019-07-18 15:37

from django.db import migrations, models
import django.db.models.deletion


def additional_info_sources(apps, schema_editor):
    """Create new InfoSource entries"""

    InfoSource = apps.get_model('workshops', 'InfoSource')

    data = [
        'Received an email or saw a flyer about The Carpentries',
        'Read about The Carpentries in a newsletter or on university website',
        'Saw the website for '
        '<a href="https://carpentries.org/">carpentries.org</a>, '
        '<a href="https://datacarpentry.org/">datacarpentry.org</a>, '
        '<a href="https://librarycarpentry.org/">librarycarpentry.org</a>, '
        'or '
        '<a href="https://software-carpentry.org/">software-carpentry.org</a>',
        'My advisor or supervisor told me about The Carpentries',
        'A friend or colleague told me about The Carpentries',
        'Saw The Carpentries on social media (Twitter, Facebook, etc.)',
        'Heard about The Carpentries at a conference, meeting, or seminar',
        'Heard about The Carpentries from a funding organization or program office',
    ]

    for entry in data:
        InfoSource.objects.create(name=entry)


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0184_auto_20190416_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text="Source description (eg. 'colleague told me')", max_length=300, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Information source',
                'verbose_name_plural': 'Information sources',
                'ordering': ['id'],
            },
        ),
        migrations.RunPython(additional_info_sources),
    ]
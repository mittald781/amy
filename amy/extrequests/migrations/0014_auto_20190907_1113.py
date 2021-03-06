# Generated by Django 2.1.7 on 2019-09-07 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('extrequests', '0013_selforganizedsubmission_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selforganizedsubmission',
            name='additional_contact',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Is there anyone you would like included on communication for this workshop? Please provide e-mail addresses.'),
        ),
        migrations.AlterField(
            model_name='selforganizedsubmission',
            name='family',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Family (last) name'),
        ),
        migrations.AlterField(
            model_name='selforganizedsubmission',
            name='institution_department',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Department/School/Library affiliation (if applicable)'),
        ),
        migrations.AlterField(
            model_name='selforganizedsubmission',
            name='personal',
            field=models.CharField(max_length=255, verbose_name='Personal (first) name'),
        ),
        migrations.AlterField(
            model_name='workshopinquiryrequest',
            name='academic_levels',
            field=models.ManyToManyField(blank=True, help_text='If you know the academic level(s) of your attendees, indicate them here. Check all that apply.', to='workshops.AcademicLevel', verbose_name="Attendees' academic level / career stage"),
        ),
        migrations.AlterField(
            model_name='workshopinquiryrequest',
            name='additional_contact',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Is there anyone you would like included on communication for this workshop? Please provide e-mail addresses.'),
        ),
        migrations.AlterField(
            model_name='workshopinquiryrequest',
            name='carpentries_info_source',
            field=models.ManyToManyField(blank=True, help_text='Check all that apply.', to='workshops.InfoSource', verbose_name='How did you hear about The Carpentries?'),
        ),
        migrations.AlterField(
            model_name='workshopinquiryrequest',
            name='computing_levels',
            field=models.ManyToManyField(blank=True, help_text="Indicate the attendees' level of computing experience, if known. We will ask attendees to fill in a skills survey before the workshop, so this answer can be an approximation. Check all that apply.", to='workshops.ComputingExperienceLevel', verbose_name="Attendees' level of computing experience"),
        ),
        migrations.AlterField(
            model_name='workshopinquiryrequest',
            name='domains',
            field=models.ManyToManyField(blank=True, help_text="The attendees' academic field(s) of study, if known. Check all that apply.", to='workshops.KnowledgeDomain', verbose_name='Domains or topic of interest for target audience'),
        ),
        migrations.AlterField(
            model_name='workshopinquiryrequest',
            name='family',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Family (last) name'),
        ),
        migrations.AlterField(
            model_name='workshopinquiryrequest',
            name='institution_department',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Department/School/Library affiliation (if applicable)'),
        ),
        migrations.AlterField(
            model_name='workshopinquiryrequest',
            name='institution_restrictions',
            field=models.CharField(blank=True, choices=[('', 'Not sure yet.'), ('no_restrictions', 'No restrictions.'), ('other', 'Other:')], default='', max_length=20, verbose_name='Our instructors live, teach, and travel globally. We understand that institutions may have citizenship, confindentiality agreements or other requirements for employees or volunteers who facilitate workshops. If your institution fits this description, please share your requirements or note that there are no restrictions.'),
        ),
        migrations.AlterField(
            model_name='workshopinquiryrequest',
            name='language',
            field=models.ForeignKey(blank=True, help_text='Our workshops are offered primarily in English, with a few of our lessons available in Spanish. While materials are mainly in English, we know it can be valuable to have an instructor who speaks the native language of the learners. We will attempt to locate Instructors speaking a particular language, but cannot guarantee the availability of non-English speaking Instructors.', null=True, on_delete=django.db.models.deletion.PROTECT, to='workshops.Language', verbose_name='What is the preferred language of communication for the workshop?'),
        ),
        migrations.AlterField(
            model_name='workshopinquiryrequest',
            name='personal',
            field=models.CharField(max_length=255, verbose_name='Personal (first) name'),
        ),
        migrations.AlterField(
            model_name='workshopinquiryrequest',
            name='routine_data',
            field=models.ManyToManyField(blank=True, help_text='Check all that apply.', to='extrequests.DataVariant', verbose_name='What kinds of data does your target audience routinely work with?'),
        ),
        migrations.AlterField(
            model_name='workshopinquiryrequest',
            name='travel_expences_agreement',
            field=models.BooleanField(default=False, verbose_name='Regardless of the fee due to The Carpentries, I understand I am also responsible for travel costs for the Instructors which can include airfare, ground travel, hotel, and meals/incidentals. I understand local Instructors will be prioritized but not guaranteed. Instructor travel costs are managed directly between the host site and the Instructors, not through The Carpentries. I will share detailed information regarding policies and procedures for travel arrangements with instructors. All reimbursements will be completed within 60 days of the workshop.'),
        ),
    ]

# Generated by Django 2.1.5 on 2019-02-18 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20190211_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_application',
            name='job_app_status',
            field=models.CharField(choices=[('U', 'Unprocessed'), ('S', 'Shortlisted'), ('N', 'Not Shortlisted')], default='U', max_length=1),
        ),
    ]

# Generated by Django 2.1.5 on 2019-02-07 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190206_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_seeker',
            name='name',
            field=models.CharField(default='name', max_length=30),
        ),
    ]

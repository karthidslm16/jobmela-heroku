# Generated by Django 2.1.5 on 2019-02-05 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0003_auto_20190203_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('job_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('job_name', models.CharField(max_length=30)),
                ('job_desc', models.CharField(max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='recruiter',
            name='id',
        ),
        migrations.AlterField(
            model_name='recruiter',
            name='email',
            field=models.EmailField(max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='job',
            name='job_poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.recruiter'),
        ),
    ]

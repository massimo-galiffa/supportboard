# Generated by Django 4.1.5 on 2023-01-11 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supportboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supportrequest',
            name='status',
            field=models.CharField(default='Aktiv', max_length=254),
        ),
    ]

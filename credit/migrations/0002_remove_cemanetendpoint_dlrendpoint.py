# Generated by Django 3.1 on 2020-09-01 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cemanetendpoint',
            name='dlrEndpoint',
        ),
    ]

# Generated by Django 3.1 on 2020-09-01 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0002_remove_cemanetendpoint_dlrendpoint'),
    ]

    operations = [
        migrations.AddField(
            model_name='cemanetendpoint',
            name='dlrEndpoint',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

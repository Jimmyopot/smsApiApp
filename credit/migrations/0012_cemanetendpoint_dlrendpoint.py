# Generated by Django 3.1 on 2020-09-18 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0011_callbackurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='cemanetendpoint',
            name='dlrEndpoint',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

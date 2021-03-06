# Generated by Django 3.1 on 2020-09-04 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0007_auto_20200902_1551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cemanetendpoint',
            old_name='my_api_key',
            new_name='api_key',
        ),
        migrations.RenameField(
            model_name='cemanetendpoint',
            old_name='my_api_secret',
            new_name='api_secret',
        ),
        migrations.RenameField(
            model_name='cemanetendpoint',
            old_name='my_clientId',
            new_name='clientId',
        ),
        migrations.RenameField(
            model_name='cemanetendpoint',
            old_name='my_message',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='cemanetendpoint',
            old_name='my_dlrEndpoint',
            new_name='phone_no',
        ),
        migrations.RenameField(
            model_name='cemanetendpoint',
            old_name='my_msisdn',
            new_name='productId',
        ),
        migrations.RenameField(
            model_name='cemanetendpoint',
            old_name='my_productId',
            new_name='unique_ref',
        ),
        migrations.RemoveField(
            model_name='cemanetendpoint',
            name='my_unique_ref',
        ),
    ]

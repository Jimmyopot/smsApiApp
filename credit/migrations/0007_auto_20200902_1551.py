# Generated by Django 3.1 on 2020-09-02 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0006_auto_20200902_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cemanetendpoint',
            name='my_api_key',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cemanetendpoint',
            name='my_api_secret',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cemanetendpoint',
            name='my_clientId',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cemanetendpoint',
            name='my_dlrEndpoint',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cemanetendpoint',
            name='my_msisdn',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cemanetendpoint',
            name='my_productId',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cemanetendpoint',
            name='my_unique_ref',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
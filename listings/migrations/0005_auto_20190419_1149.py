# Generated by Django 2.1.7 on 2019-04-19 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_listing_brochure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='brochure',
            field=models.FileField(null=True, upload_to='files/%Y/%m/%d/'),
        ),
    ]

# Generated by Django 2.1.7 on 2019-04-08 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20190408_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='display_img',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
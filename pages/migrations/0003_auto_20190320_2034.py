# Generated by Django 2.1.7 on 2019-03-20 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
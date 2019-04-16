# Generated by Django 2.1.7 on 2019-03-21 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_delete_carousel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('display_Image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
            ],
        ),
    ]
# Generated by Django 3.2.6 on 2023-04-06 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(height_field=100, upload_to='images/', width_field=100),
        ),
    ]

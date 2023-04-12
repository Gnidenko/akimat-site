# Generated by Django 3.2.6 on 2023-04-06 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_post_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(upload_to='images/preview/'),
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='post_images/')),
                ('caption', models.CharField(blank=True, max_length=200)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='news.post')),
            ],
            options={
                'verbose_name_plural': 'Post Images',
            },
        ),
    ]

# Generated by Django 5.2 on 2025-05-08 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, default='basic-crystal-polygon-art-g0q6akxrkqfh86zo.jpg', upload_to='banners/'),
        ),
    ]

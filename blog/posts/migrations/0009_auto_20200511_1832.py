# Generated by Django 3.0.6 on 2020-05-11 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_post_videos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='videos',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-28 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0038_auto_20200527_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='profile_pic'),
        ),
    ]

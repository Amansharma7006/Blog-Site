# Generated by Django 3.0.6 on 2020-05-27 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0032_auto_20200527_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profile_pic',
            field=models.ImageField(default='default.png', upload_to='profile_pic'),
        ),
    ]

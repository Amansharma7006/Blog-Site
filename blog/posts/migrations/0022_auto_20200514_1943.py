# Generated by Django 3.0.6 on 2020-05-14 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0021_auto_20200514_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Publihsed', 'Publihsed')], max_length=9),
        ),
    ]

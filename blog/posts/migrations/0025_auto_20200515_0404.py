# Generated by Django 3.0.6 on 2020-05-14 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0024_auto_20200514_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('publihsed', 'Publihsed')], max_length=9),
        ),
    ]

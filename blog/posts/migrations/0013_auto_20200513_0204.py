# Generated by Django 3.0.6 on 2020-05-12 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0012_remove_post_comment_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(default='True', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

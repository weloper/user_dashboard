# Generated by Django 2.0.6 on 2018-08-03 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('haikuapp', '0003_auto_20180803_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivate',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

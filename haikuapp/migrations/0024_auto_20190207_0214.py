# Generated by Django 2.1 on 2019-02-07 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haikuapp', '0023_auto_20180816_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='user_input',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cardfield',
            name='variable',
            field=models.CharField(default='asdf', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='template',
            name='preview_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='template',
            name='template_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='template',
            name='vertical',
            field=models.CharField(choices=[('generic', 'generic'), ('gym', 'gym'), ('pharma', 'pharma'), ('food', 'food')], default='text', max_length=255),
        ),
        migrations.AddField(
            model_name='templatefields',
            name='varRequired',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='templatefields',
            name='varType',
            field=models.CharField(choices=[('textarea', 'Textarea'), ('text', 'Text'), ('checkbox', 'Checkbox'), ('radio', 'Radio'), ('date', 'Date'), ('time', 'Time'), ('number', 'Number'), ('color', 'Color'), ('range', 'Range'), ('image', 'Image'), ('video', 'Video')], default='text', max_length=255),
        ),
        migrations.AddField(
            model_name='templatefields',
            name='variable',
            field=models.CharField(default='asdf', max_length=255),
            preserve_default=False,
        ),
    ]

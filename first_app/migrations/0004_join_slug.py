# Generated by Django 3.0.8 on 2020-08-12 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_join_ref_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]

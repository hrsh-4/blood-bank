# Generated by Django 2.2 on 2020-12-04 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_auto_20201203_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='is_requested',
            field=models.BooleanField(default=False),
        ),
    ]

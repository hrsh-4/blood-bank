# Generated by Django 2.2 on 2020-12-04 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_hospital_is_requested'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bank.Hospital'),
        ),
        migrations.AlterField(
            model_name='request',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bank.Receiver'),
        ),
    ]

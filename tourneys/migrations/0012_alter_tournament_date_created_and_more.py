# Generated by Django 4.0.4 on 2022-10-07 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourneys', '0011_tournament_date_created_tournament_date_ended_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='date_created',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='date_ended',
            field=models.DateField(null=True),
        ),
    ]

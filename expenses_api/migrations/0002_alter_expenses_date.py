# Generated by Django 4.0.3 on 2022-04-15 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(),
        ),
    ]

# Generated by Django 3.2.5 on 2021-11-29 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 3.2 on 2021-04-19 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corredor',
            name='codigo',
            field=models.IntegerField(),
        ),
    ]

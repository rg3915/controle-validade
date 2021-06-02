# Generated by Django 3.2 on 2021-04-20 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_funcionario_filial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ['descricao']},
        ),
        migrations.AlterModelOptions(
            name='funcionario',
            options={'ordering': ['usuario']},
        ),
        migrations.AddField(
            model_name='corredor',
            name='slug',
            field=models.SlugField(default='teste', max_length=30),
        ),
        migrations.AddField(
            model_name='filial',
            name='slug',
            field=models.SlugField(default='teste', max_length=30),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='slug',
            field=models.SlugField(default='teste'),
        ),
    ]

# Generated by Django 3.2 on 2021-04-19 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_user_funcionario_usuario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filial',
            options={'verbose_name_plural': 'Filiais'},
        ),
        migrations.AddField(
            model_name='funcionario',
            name='filial',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='filial', to='main.filial'),
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-21 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicos',
            name='servico',
            field=models.CharField(default='new', max_length=100, verbose_name='Serviço'),
        ),
    ]

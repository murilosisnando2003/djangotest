# Generated by Django 2.1 on 2018-08-04 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_fornecedores_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='fornecedores',
            name='status',
            field=models.CharField(choices=[('1', 'Ativo'), ('2', 'Desativado')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fornecedores',
            name='telefone',
            field=models.CharField(blank=True, default=1, max_length=20),
        ),
    ]

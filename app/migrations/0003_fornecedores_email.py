# Generated by Django 2.1 on 2018-08-04 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180803_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='fornecedores',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
    ]

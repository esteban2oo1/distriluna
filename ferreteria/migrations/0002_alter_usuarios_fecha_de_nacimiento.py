# Generated by Django 4.2.4 on 2023-10-31 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferreteria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='fecha_de_nacimiento',
            field=models.DateTimeField(),
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-22 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_domicilio_persona_domicilio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='Domicilio',
            new_name='domicilio',
        ),
    ]

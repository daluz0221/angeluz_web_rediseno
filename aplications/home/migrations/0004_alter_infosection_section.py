# Generated by Django 3.2 on 2024-03-31 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_redessociales_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infosection',
            name='section',
            field=models.CharField(choices=[('1', 'sobre mi'), ('2', 'faq'), ('3', 'entradas'), ('4', 'servicios'), ('5', 'contacto')], max_length=1, verbose_name='Sección'),
        ),
    ]

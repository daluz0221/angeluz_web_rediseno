# Generated by Django 3.2 on 2024-03-31 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_headerlinks_infohome_infosection_redessociales'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='redessociales',
            name='name',
        ),
    ]
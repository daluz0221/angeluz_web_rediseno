# Generated by Django 3.2 on 2024-04-06 17:26

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_service_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Contenido'),
        ),
    ]
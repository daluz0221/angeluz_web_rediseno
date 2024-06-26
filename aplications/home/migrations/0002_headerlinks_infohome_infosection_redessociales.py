# Generated by Django 3.2 on 2024-03-31 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
                ('orden', models.SmallIntegerField(default=0, verbose_name='Orden')),
                ('active', models.BooleanField(default=False, verbose_name='Activo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'enlace del menú',
                'verbose_name_plural': 'enlaces del menú',
                'ordering': ['-orden'],
            },
        ),
        migrations.CreateModel(
            name='InfoHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('webTitle', models.CharField(help_text='texto que se mostrará en la pestaña del navegador', max_length=200, verbose_name='Título de la web')),
                ('logoHome', models.ImageField(blank=True, null=True, upload_to='home', verbose_name='Logo de la web')),
                ('eslogan', models.CharField(blank=True, max_length=200, null=True, verbose_name='Eslogan')),
                ('active', models.BooleanField(default=False, verbose_name='Activo')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='Teléfono')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo electrónico')),
                ('mainUrl', models.URLField(blank=True, null=True, verbose_name='URL principal')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'información de la página de inicio',
                'verbose_name_plural': 'información de la página de inicio',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='InfoSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(choices=[('1', 'home'), ('2', 'faq'), ('3', 'entradas'), ('4', 'servicios'), ('5', 'contacto'), ('6', 'sobre mi')], max_length=1, verbose_name='Sección')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Título')),
                ('subtitle', models.CharField(blank=True, max_length=200, null=True, verbose_name='Subtítulo')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Contenido')),
                ('image', models.ImageField(blank=True, null=True, upload_to='home', verbose_name='Imagen')),
                ('active', models.BooleanField(default=False, verbose_name='Activo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'información de sección',
                'verbose_name_plural': 'información de secciones',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='RedesSociales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('icon', models.CharField(choices=[('facebook', 'facebook'), ('twitter', 'twitter'), ('instagram', 'instagram'), ('linkedin', 'linkedin'), ('youtube', 'youtube'), ('whatsapp', 'whatsapp'), ('telegram', 'telegram'), ('github', 'github'), ('gitlab', 'gitlab'), ('bitbucket', 'bitbucket'), ('tiktok', 'tiktok')], max_length=20, verbose_name='Icono')),
                ('orden', models.SmallIntegerField(default=0, verbose_name='Orden')),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
                ('active', models.BooleanField(default=False, verbose_name='Activo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'red social',
                'verbose_name_plural': 'redes sociales',
                'ordering': ['-created'],
            },
        ),
    ]

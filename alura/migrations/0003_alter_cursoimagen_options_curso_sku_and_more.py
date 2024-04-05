# Generated by Django 5.0.3 on 2024-03-21 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alura', '0002_cursoimagen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cursoimagen',
            options={'verbose_name_plural': 'Imagenes del Curso'},
        ),
        migrations.AddField(
            model_name='curso',
            name='sku',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='curso',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='dificultad',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='duracion',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='estudiantes',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='idioma',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nota_a',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nota_b',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nota_c',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='profesor',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='subtitulo',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
# Generated by Django 5.0.3 on 2024-04-10 02:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alura', '0014_alter_comentario_curso_alter_comentario_usuario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alura.curso'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='usuario',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
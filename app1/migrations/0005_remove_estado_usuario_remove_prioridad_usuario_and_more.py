# Generated by Django 4.1.7 on 2023-03-27 05:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0004_alter_ticket_departamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estado',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='prioridad',
            name='usuario',
        ),
        migrations.AddField(
            model_name='estado',
            name='fecha_modificacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='estado',
            name='usuario_creacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='estados_creados', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='estado',
            name='usuario_modificacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='estados_modificados', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='prioridad',
            name='fecha_modificacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='prioridad',
            name='usuario_creacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='prioridades_creadas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='prioridad',
            name='usuario_modificacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='prioridades_modificadas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='estado',
            name='FK_id_ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estados', to='app1.ticket'),
        ),
        migrations.AlterField(
            model_name='prioridad',
            name='FK_id_ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prioridades', to='app1.ticket'),
        ),
    ]

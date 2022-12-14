# Generated by Django 4.1 on 2022-08-29 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_linea_descripcion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='linea',
            options={'ordering': ('id',), 'verbose_name': 'Linea Producto', 'verbose_name_plural': 'Lineas Productos'},
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100, unique=True, verbose_name='Grupo')),
                ('image', models.FileField(blank=True, null=True, upload_to='core/grupo', verbose_name='Foto')),
                ('estado', models.BooleanField(default=True)),
                ('linea', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.linea')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'ordering': ('id',),
            },
        ),
    ]

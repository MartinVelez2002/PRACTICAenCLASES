# Generated by Django 4.1 on 2022-08-29 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_grupo_linea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='linea',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.linea'),
        ),
    ]

# Generated by Django 4.1 on 2022-08-29 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_linea_options_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='linea',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.linea'),
        ),
    ]

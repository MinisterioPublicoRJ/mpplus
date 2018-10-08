# Generated by Django 2.1.2 on 2018-10-05 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mpplus_rest', '0009_auto_20181005_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tema',
            name='area_mae',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='temas', to='mpplus_rest.Area'),
        ),
        migrations.AlterField(
            model_name='tema',
            name='areas_correlatas',
            field=models.ManyToManyField(related_name='temas_correlatos', to='mpplus_rest.Area'),
        ),
    ]

# Generated by Django 2.1.2 on 2018-10-03 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mpplus_rest', '0003_remove_area_icone'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='icone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mpplus_rest.Icone'),
        ),
        migrations.AddField(
            model_name='area',
            name='prioridade',
            field=models.IntegerField(default=1),
        ),
    ]

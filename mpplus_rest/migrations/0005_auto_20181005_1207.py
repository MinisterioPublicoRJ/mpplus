# Generated by Django 2.1.2 on 2018-10-05 15:07

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpplus_rest', '0004_auto_20181003_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='icone',
            name='file_name',
            field=models.CharField(default='replace', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='area',
            name='cor',
            field=colorfield.fields.ColorField(default='#FF0000', max_length=18),
        ),
    ]

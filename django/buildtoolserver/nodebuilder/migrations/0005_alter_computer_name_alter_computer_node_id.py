# Generated by Django 4.0.6 on 2022-08-07 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodebuilder', '0004_remove_node_sql_id_computer_icon_computer_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='name',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='computer',
            name='node_id',
            field=models.CharField(default=None, max_length=255),
        ),
    ]

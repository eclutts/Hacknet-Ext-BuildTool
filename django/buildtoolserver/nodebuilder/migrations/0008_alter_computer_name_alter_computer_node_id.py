# Generated by Django 4.0.6 on 2022-08-11 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodebuilder', '0007_alter_computer_name_alter_computer_node_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='node_id',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
# Generated by Django 4.0.2 on 2022-03-01 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0004_rename_module_moduleleaders_module_instance_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ratings',
            old_name='module_leaders',
            new_name='module_leader',
        ),
    ]
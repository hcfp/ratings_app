# Generated by Django 4.0.2 on 2022-03-01 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_remove_ratings_submitting_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moduleleaders',
            old_name='module',
            new_name='module_instance',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='module_instance',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='professor',
        ),
        migrations.AddField(
            model_name='ratings',
            name='module_leaders',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ratings.moduleleaders'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-29 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0013_rename_initial_initial_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='dateoj',
            new_name='doj',
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0014_rename_dateoj_employee_doj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='doj',
            field=models.DateField(auto_now_add=True),
        ),
    ]
# Generated by Django 4.1.1 on 2022-09-29 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0016_alter_department_options_alter_employee_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='doj',
            field=models.DateField(),
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-29 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0009_alter_department_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.FloatField(),
        ),
    ]

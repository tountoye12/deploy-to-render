# Generated by Django 5.1 on 2024-08-11 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_employee_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='groudId',
            field=models.IntegerField(),
        ),
    ]

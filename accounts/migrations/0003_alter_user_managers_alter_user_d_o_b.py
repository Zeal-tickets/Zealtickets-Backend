# Generated by Django 5.0.7 on 2024-08-04 06:32

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_password'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='d_o_b',
            field=models.DateField(null=True),
        ),
    ]

# Generated by Django 5.0.7 on 2024-08-03 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_password'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
    ]

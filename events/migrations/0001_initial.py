# Generated by Django 5.0.7 on 2024-08-03 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_alter_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_attendees', models.IntegerField()),
                ('venue', models.CharField(max_length=1000)),
                ('datetime', models.DateTimeField()),
                ('deadline', models.DateTimeField()),
                ('description', models.TextField(max_length=2000)),
                ('poster', models.FileField(upload_to='')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.categories')),
                ('sellerprofile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.sellerprofile')),
            ],
        ),
    ]

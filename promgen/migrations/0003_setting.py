# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 07:50


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promgen', '0002_audit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=128)),
                ('value', models.CharField(max_length=128)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-10 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=40)),
                ('image_description', models.CharField(max_length=100)),
                ('image_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='image_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Location'),
        ),
    ]

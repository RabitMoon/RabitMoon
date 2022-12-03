# Generated by Django 4.1.3 on 2022-12-03 03:53

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_datastructure'),
    ]

    operations = [
        migrations.CreateModel(
            name='DBMS',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('Content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('slug', models.CharField(max_length=130)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='digitalElectronics',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('Content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('slug', models.CharField(max_length=130)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Maths',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('Content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('slug', models.CharField(max_length=130)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Oop',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('Content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('slug', models.CharField(max_length=130)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
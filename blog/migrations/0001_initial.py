# Generated by Django 4.1.3 on 2022-12-01 05:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('Auth', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=225)),
                ('time', models.DateTimeField(auto_now=True)),
                ('Content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('slug', models.CharField(max_length=130)),
            ],
        ),
    ]

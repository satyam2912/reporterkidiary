# Generated by Django 2.2.12 on 2021-05-01 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporterKidiary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='url',
            field=models.SlugField(unique=True),
        ),
    ]

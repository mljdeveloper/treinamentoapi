# Generated by Django 4.0.4 on 2022-06-17 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttunitimage', '0002_remove_ttunitimage_description_ttunitimage_parent_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ttunitimage',
            name='slug',
            field=models.SlugField(null=True, unique=True, verbose_name='Atalho'),
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-09 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttowner', '0003_ttowner_pkowner_email_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ttowner',
            name='slug',
            field=models.SlugField(null=True, unique=True, verbose_name='Atalho'),
        ),
    ]
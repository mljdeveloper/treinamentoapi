# Generated by Django 4.0.4 on 2022-04-28 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_remove_user_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='parent_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

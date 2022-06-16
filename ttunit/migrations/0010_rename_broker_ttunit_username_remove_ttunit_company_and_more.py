# Generated by Django 4.0.4 on 2022-06-16 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ttunit', '0009_alter_ttunit_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ttunit',
            old_name='broker',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='ttunit',
            name='company',
        ),
        migrations.AddField(
            model_name='ttunit',
            name='parent_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='parentid_ttunit', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

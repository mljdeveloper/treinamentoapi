# Generated by Django 4.0.4 on 2022-05-06 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Frequency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('days', models.IntegerField()),
                ('display', models.BooleanField(default=True)),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='username_frequency_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'frequency',
                'verbose_name_plural': 'frequencies',
                'ordering': ('name',),
            },
        ),
    ]

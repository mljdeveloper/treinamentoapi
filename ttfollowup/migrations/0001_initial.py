# Generated by Django 4.0.4 on 2022-06-16 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ttlead', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TTfollowup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(null=True, unique=True, verbose_name='Atalho')),
                ('description', models.TextField(blank=True, max_length=4000, null=True)),
                ('lead', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ttfollowup_ttlead', to='ttlead.ttlead')),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ttfollowup_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Followup',
                'verbose_name_plural': 'Followups',
                'ordering': ('username',),
            },
        ),
    ]

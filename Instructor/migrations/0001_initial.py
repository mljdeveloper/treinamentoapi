# Generated by Django 4.0.4 on 2022-05-03 13:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Zipcode', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=100, verbose_name='Slug')),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=10)),
                ('codearea', models.CharField(blank=True, max_length=4, null=True)),
                ('phonenumber', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('display', models.BooleanField(default=True)),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='username_instructor_set', to=settings.AUTH_USER_MODEL)),
                ('zipcode', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Zipcode.zipcode')),
            ],
            options={
                'verbose_name': 'Instructor',
                'verbose_name_plural': 'Instructors',
                'ordering': ('name',),
            },
        ),
    ]

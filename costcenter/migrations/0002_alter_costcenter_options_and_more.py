# Generated by Django 4.0.4 on 2022-05-26 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costcenter', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='costcenter',
            options={},
        ),
        migrations.AlterField(
            model_name='costcenter',
            name='costcentercod',
            field=models.CharField(max_length=10),
        ),
        migrations.AddConstraint(
            model_name='costcenter',
            constraint=models.UniqueConstraint(fields=('costcentercod', 'username'), name='PKCostCenter_CostCenterCod_UserName'),
        ),
    ]

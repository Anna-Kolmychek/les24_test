# Generated by Django 4.2.5 on 2023-09-30 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]

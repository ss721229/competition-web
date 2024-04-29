# Generated by Django 5.0.4 on 2024-04-29 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='platform',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='competition',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='competition',
            name='url',
            field=models.URLField(),
        ),
    ]

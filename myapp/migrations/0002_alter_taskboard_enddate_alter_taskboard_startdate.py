# Generated by Django 5.1.4 on 2024-12-30 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskboard',
            name='endDate',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='taskboard',
            name='startDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# Generated by Django 2.2 on 2023-09-26 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='body',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='header',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

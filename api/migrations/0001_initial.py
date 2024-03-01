# Generated by Django 2.2 on 2023-09-07 11:14

import datetime
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
            name='BlogModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('header', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, default=None, upload_to='')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(default=None, max_length=100)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.BlogModel')),
            ],
        ),
    ]
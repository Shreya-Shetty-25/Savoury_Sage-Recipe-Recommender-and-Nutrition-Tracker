# Generated by Django 5.1 on 2024-09-16 19:41

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('ingredients', models.TextField()),
                ('calories', models.FloatField(default=0)),
                ('fat', models.FloatField(default=0)),
                ('saturated_fat', models.FloatField(default=0)),
                ('carbohydrates', models.FloatField(default=0)),
                ('sugar', models.FloatField(default=0)),
                ('cholesterol', models.FloatField(default=0)),
                ('sodium', models.FloatField(default=0)),
                ('protein', models.FloatField(default=0)),
                ('date_prepared', models.DateField(default=datetime.date.today)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 5.1.5 on 2025-02-16 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='views_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Views Count'),
        ),
    ]

# Generated by Django 5.1.5 on 2025-02-15 12:32

import django.core.validators
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
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Brief Description')),
                ('author', models.CharField(max_length=255, verbose_name='Author')),
                ('category', models.CharField(max_length=100, verbose_name='Category')),
                ('book_file', models.FileField(upload_to='books/files/', verbose_name='Book File')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Link')),
                ('poster_image', models.ImageField(upload_to='books/posters/', verbose_name='Poster Image')),
                ('publish_date', models.DateField(verbose_name='Publish Date')),
                ('total_pages', models.PositiveIntegerField(verbose_name='Total Pages')),
                ('language', models.CharField(max_length=50, verbose_name='Language')),
                ('rating', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Rating')),
                ('reviews_count', models.PositiveIntegerField(default=0, verbose_name='Reviews Count')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=20, verbose_name='Status')),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Added By')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
    ]

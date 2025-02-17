from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

class Book(models.Model):

    STATUS = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=255, verbose_name="Title")
    description = models.TextField(verbose_name="Brief Description")
    author = models.CharField(max_length=255, verbose_name="Author")
    category = models.CharField(max_length=100, verbose_name="Category")
    book_file = models.FileField(upload_to='books/files/', verbose_name="Book File")
    link = models.URLField(blank=True, null=True, verbose_name="Link")
    poster_image = models.ImageField(upload_to='books/posters/', verbose_name="Poster Image")
    publish_date = models.DateField(verbose_name="Publish Date")
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Added By")
    total_pages = models.PositiveIntegerField(verbose_name="Total Pages")
    language = models.CharField(max_length=50, verbose_name="Language")
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        default=0,
        verbose_name="Rating"
    )
    reviews_count = models.PositiveIntegerField(default=0, verbose_name="Reviews Count")
    status = models.CharField(max_length=20, choices=STATUS, default='draft', verbose_name="Status")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Views Count")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
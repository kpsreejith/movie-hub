from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=10, unique=True)
    slug = models.SlugField()

    def get_url(self):
        return reverse('app:movie_by_category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.category)


class Movies(models.Model):
    movie = models.CharField(max_length=30, unique=True, null=False)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    release_date = models.DateField()
    description = models.TextField()
    cast = models.TextField(blank=True)
    imdb_rating = models.IntegerField()
    trailer_link = models.URLField(blank=True)
    image = models.ImageField(upload_to="image")
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    comments_or_review = models.TextField(blank=True)

    def __str__(self):
        return self.movie

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

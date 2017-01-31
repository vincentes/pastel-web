from django.db import models
from django.core.validators import MinValueValidator


class Album(models.Model):
    name = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    album_logo = models.CharField(max_length=1000)
    year = models.IntegerField(validators=[
        MinValueValidator(1)
    ])

    def __str__(self):
        return "{0} - {1}".format(self.artist, self.name)


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title

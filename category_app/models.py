from django.db import models

# Create your models here.


class Category(models.Model):
    tittle = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.tittle


class Artist(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='artist_image')
    category = models.ManyToManyField(Category, related_name='artists')

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='album_image')
    release_date = models.IntegerField(null=True)
    artist = models.ManyToManyField(Artist, related_name='albums')

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=100, null=True)
    song = models.FileField(upload_to='songs', null=True, blank=True)
    image = models.ImageField(upload_to='images')
    artist_name = models.CharField(max_length=100, null=True)
    artist = models.ManyToManyField(Artist, related_name='songs')
    category = models.ManyToManyField(Category, related_name='songs')
    release_date = models.IntegerField(null=True)
    album = models.ManyToManyField(Album, related_name='songs')
    album_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

    

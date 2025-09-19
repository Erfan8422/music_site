from django.contrib import admin
from .models import Song, Artist, Category, Album

# Register your models here.

admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Category)
admin.site.register(Album)
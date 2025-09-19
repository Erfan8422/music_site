from django.shortcuts import render, get_object_or_404
from .models import Song, Artist, Category, Album
from django.core.paginator import Paginator

def song(request):
    categories = Category.objects.all()
    artists = Artist.objects.all()
    songs = Song.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(artists, 3)
    artists_list = paginator.get_page(page_number)
    return render(request, 'artists.html', context={'songs': songs, 'artists': artists_list, 'cats': categories})

def artist(request, pk=None):
    categories = Category.objects.all()
    artist = Artist.objects.get(id=pk)
    albums = artist.albums.all()
    songs = artist.songs.all()
    return render(request, 'cat2.html', context={'songs': songs, 'artist': artist, 'cats': categories, 'albums':albums})

def category(request, pk=None):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=pk)
    artists = category.artists.all()
    page_number = request.GET.get('page')
    paginator = Paginator(artists, 3)
    artists_list = paginator.get_page(page_number)
    songs = category.songs.all()
    return render(request, 'artists.html', context={'songs': songs, 'artists': artists_list, 'cats': categories})

def album(request, pk=None):
    categories = Category.objects.all()
    album = Album.objects.get(id=pk)
    artist = album.artist.all()
    songs = album.songs.all()
    return render(request, 'cat3.html', context={'songs': songs, 'artist': artist, 'cats': categories, 'album':album})


def base(request):
    categories = Category.objects.all()
    return render(request, 'base.html', context={'cats':categories})

def search(request):
    q = request.GET.get('q')
    artists_list = Artist.objects.filter(name__icontains=q)
    return render(request, 'artists.html', context={'artists': artists_list})
 

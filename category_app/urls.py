from django.urls import path
from . import views

app_name = 'category_app'

urlpatterns = [
    path('category/<int:pk>', views.category, name='category'),
    path('artists', views.song, name='artists'),
    path('artist/<int:pk>', views.artist, name='artist'),
    path('album/<int:pk>', views.album, name='album'),
    path('base/<int:pk>', views.base, name='cat'),
    path('search', views.search, name='search'),
    
]

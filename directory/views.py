from django.views import generic
from .models import Album


class IndexView(generic.ListView):
    model = Album
    context_object_name = 'all_albums'
    template_name = 'tunes/index.html'

    def get_queryset(self):
        return Album.objects.all()


class AlbumView(generic.DetailView):
    model = Album
    template_name = 'tunes/album.html'

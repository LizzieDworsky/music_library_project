from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import SongSerializer
from .models import Song

# Create your views here.

@api_view(["GET"])
def songs_list(request):
    
    if request.method == "GET":
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def song_details(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == "GET":
        serializer = SongSerializer(song)
        return Response(serializer.data)
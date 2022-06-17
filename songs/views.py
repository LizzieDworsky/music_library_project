from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import SongSerializer
from .models import Song

# Create your views here.

@api_view(["GET", "POST"])
def songs_list(request):
    
    if request.method == "GET":                                             #checking the request type
        songs = Song.objects.all()                                          #querying the database for all objects in the Song table
        serializer = SongSerializer(songs, many=True)                       #serializing the data (to json) using two params songs is the array of data retrieved on previous line, many=True is telling it to anticipate multiple objects
        return Response(serializer.data, status=status.HTTP_200_OK)         #responding to the request with the serialized data and the hard coded 200 status
    elif request.method == "POST":                                          #checking the request type
        serializer = SongSerializer(data=request.data)                      #converting the json data passed in through the POST method to python object data
        serializer.is_valid(raise_exception=True)                           #checking if the data is valid before the next step
        serializer.save()                                                   #once the object data has been verified, saving it to the database
        return Response(serializer.data, status=status.HTTP_201_CREATED)    #responding to the request with new data added and the hard coded 201 status


@api_view(["GET", "PUT", "DELETE"])
def song_details(request, pk):

    song = get_object_or_404(Song, pk=pk)                                   #querying the database for one object using the pk(primary key)

    if request.method == "GET":                                             #checking the request type
        serializer = SongSerializer(song)                                   #serializing the song data from the database
        return Response(serializer.data, status=status.HTTP_200_OK)         #responding to the request with the serialized data of that single object and the hard coded status of 200
    elif request.method == "PUT":                                           #checking request type
        serializer = SongSerializer(song, data=request.data)                #conversting the json data passed in to a python object
        serializer.is_valid(raise_exception=True)                           #validating the data
        serializer.save()                                                   #saving the data after validation
        return Response(serializer.data, status=status.HTTP_200_OK)         #responding to the request with the serialized data and hard coded 200 status
    elif request.method == "DELETE":                                        #checking request type
        song.delete()                                                       #removing the data permanently from the database
        return Response(status=status.HTTP_204_NO_CONTENT)                  #responding to the request with status 204, used as a confirmation the content has been removed from the database

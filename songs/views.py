from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(["GET"])
def songs_list(request):
    return Response("Hello World")


@api_view(["GET"])
def song_details(request):
    return Response("Hello World Details")
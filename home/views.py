from .serializers import LibrarySerializer
from .models import Libraries
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
# Create your views here.


@api_view(['POST'])
def create(request):
    serializer = LibrarySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(data=serializer.data)


@api_view(['GET'])
def homepage(request):
    libraries = Libraries.objects.all()
    serializer = LibrarySerializer(libraries, many=True)

    return Response(data=serializer.data)

@api_view(['GET'])
def get_url(request):
    libraries = Libraries.objects.all()
    url = []
    for i in libraries:
        url.append({"name":i.name, "url": i.url})

    return Response(data=url)


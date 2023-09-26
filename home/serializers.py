from rest_framework.serializers import ModelSerializer
from .models import Libraries

class LibrarySerializer(ModelSerializer):
    class Meta:
        model = Libraries
        fields = '__all__'


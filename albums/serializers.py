from rest_framework import serializers
from songs.serializers import SongSerializer
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["id", "name", "year", "user_id"]
        read_only_fields = ["user_id"]

    def create(self, validated_data):
        return Album.objects.create(**validated_data)

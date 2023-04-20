from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from .serializers import SongSerializer
from rest_framework import generics
from .pagination import CustomSongPageNumberPagination


class ListCreateSongView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    lookup_url_kwarg = "pk"
    pagination_class = CustomSongPageNumberPagination

    def perform_create(self, serializer):
        return serializer.save(album_id=self.kwargs.get("pk"))

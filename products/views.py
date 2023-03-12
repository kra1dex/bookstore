from rest_framework.viewsets import ModelViewSet

from products.models import Book, Genre
from products.serializers import GenreSerializer, BookSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

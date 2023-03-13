from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from products.models import Book, Author, Genre
from products.serializers import BookListCreateSerializer, AuthorSerializer, GenreSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListCreateSerializer

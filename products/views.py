from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet

from products.models import Book, Author, Genre
from products.serializers import BookListSerializer, BookCreateSerializer, BookDetailSerializer, BookUpdateSerializer,\
    BookDestroySerializer, AuthorSerializer, GenreSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer


class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer


class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer


class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookUpdateSerializer


class BookDestroyView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDestroySerializer

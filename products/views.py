from rest_framework.generics import ListAPIView, CreateAPIView

from products.models import Book
from products.serializers import BookListSerializer, BookCreateSerializer


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer


class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer

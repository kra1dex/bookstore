from rest_framework.generics import ListAPIView

from products.models import Book
from products.serializers import BookListSerializer


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer

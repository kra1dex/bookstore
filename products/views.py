from rest_framework.generics import ListCreateAPIView

from products.models import Book
from products.serializers import BookListSerializer


class BookListView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer

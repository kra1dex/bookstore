from django.http import JsonResponse
from django.views import View

from products.models import Book


class BookListView(View):
    def get(self, _):
        books = Book.objects.all()

        response = []
        for book in books:
            response.append({
                'id': book.id,
                'title': book.title,
                'price': book.price,
            })

        return JsonResponse(response, safe=False)

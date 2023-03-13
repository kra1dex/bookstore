import json
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from products.models import Book, Author, Genre
from products.serializers import BookSerializer


class BookApiTestCase(TestCase):
    def setUp(self):
        # Authors
        author1 = Author.objects.create(name='author_name', surname='author_surname')

        # Genres
        genres = [Genre(title='first'), Genre(title='second'), Genre(title='third')]
        Genre.objects.bulk_create(genres)

        # Books
        self.book1 = Book.objects.create(
            author=author1, title='test_title', description='test_description', price=100
        )
        self.book1.genres.set(genres)

    def test_get_list(self):
        path = reverse('book-list')
        response = self.client.get(path)

        serializer_data = BookSerializer([self.book1], many=True).data

        self.assertEqual(serializer_data, response.data)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_post(self):
        self.assertEqual(Book.objects.count(), 1)
        path = reverse('book-list')

        data = {
            "author": {
                "name": "test",
                "surname": "test"
            },
            "genres": [
                "test",
                "test"
            ],
            "title": "test",
            "description": "test",
            "price": "0.00"
        }
        json_data = json.dumps(data)

        response = self.client.post(path, data=json_data, content_type='application/json')

        self.assertEqual(HTTPStatus.CREATED, response.status_code)
        self.assertEqual(Book.objects.count(), 2)

    def test_get_book(self):
        path = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(path)

        book_data = BookSerializer(self.book1).data

        self.assertEqual(book_data, response.data)
        self.assertEqual(HTTPStatus.OK, response.status_code)

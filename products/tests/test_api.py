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
        book1 = Book.objects.create(
            author=author1, title='test_title', description='test_description', price=100
        )
        book1.genres.set(genres)

        # data
        self.serializer_data = BookSerializer([book1], many=True).data

    def test_get_list(self):
        path = reverse('book-list')
        response = self.client.get(path)

        self.assertEqual(self.serializer_data, response.data)
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
            "price": "00.00"
        }
        json_data = json.dumps(data)

        response = self.client.post(path, data=json_data, content_type='application/json')

        self.assertEqual(HTTPStatus.CREATED, response.status_code)
        self.assertEqual(Book.objects.count(), 2)
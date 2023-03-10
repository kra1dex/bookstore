from rest_framework import serializers

from products.models import Book, Author, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)
    genres = GenreSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'


class BookCreateSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)
    genres = GenreSerializer(required=False, many=True)

    class Meta:
        model = Book
        fields = '__all__'

    def is_valid(self, *, raise_exception=False):
        self._genres = self.initial_data.pop('genres')
        self._author = self.initial_data.pop('author')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        try:
            author_obj = Author.objects.get(name=self._author['name'], surname=self._author['surname'])
        except Author.DoesNotExist:
            if 'biography' in self._author:
                author_obj = Author.objects.create(
                    name=self._author['name'], surname=self._author['surname'], biography=self._author['biography']
                )
            else:
                author_obj = Author.objects.create(name=self._author['name'], surname=self._author['surname'])
        validated_data['author_id'] = author_obj.id

        book = Book.objects.create(**validated_data)
        for genre in self._genres:
            genre_obj, _ = Genre.objects.get_or_create(title=genre)
            book.genres.add(genre_obj)

        book.save()
        return book


class BookDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)
    genres = GenreSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializerForBookUpdate(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'surname']


class BookUpdateSerializer(serializers.ModelSerializer):
    author = AuthorSerializerForBookUpdate(required=False)
    genres = serializers.SlugRelatedField(slug_field='title', queryset=Genre.objects.all(), required=False, many=True)

    class Meta:
        model = Book
        fields = '__all__'

    def is_valid(self, *, raise_exception=False):
        self._genres = self.initial_data.pop('genres')
        self._author = self.initial_data.pop('author')
        return super().is_valid(raise_exception=raise_exception)

    def save(self, **validated_data):
        book = super().save()

        author_obj, _ = Author.objects.get_or_create(name=self._author['name'], surname=self._author['surname'])
        book.author = author_obj

        for genre in self._genres:
            genre_obj, _ = Genre.objects.get_or_create(title=genre)
            book.genres.add(genre_obj)

        book.save()
        return book


class BookDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id']

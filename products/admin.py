from django.contrib import admin

from products.models import Book, Author, Genre


@admin.register(Genre)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

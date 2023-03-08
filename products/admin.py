from django.contrib import admin

from products.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

# Generated by Django 4.1.7 on 2023-03-12 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_genre_book_genres'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='biography',
        ),
    ]

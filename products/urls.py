from django.urls import path

from products import views

urlpatterns = [
    path('books/', views.BookListView.as_view()),
]

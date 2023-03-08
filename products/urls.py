from django.urls import path

from products import views

urlpatterns = [
    path('', views.BookListView.as_view()),
]

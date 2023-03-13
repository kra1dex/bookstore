from django.urls import path, include
from rest_framework import routers

from products import views

router = routers.SimpleRouter()
router.register('genres', views.GenreViewSet)
router.register('authors', views.AuthorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('books/', views.BookListCreateView.as_view()),
    path('books/<int:pk>/', views.BookDetailView.as_view()),
    path('books/<int:pk>/update/', views.BookUpdateView.as_view()),
    path('books/<int:pk>/delete/', views.BookDestroyView.as_view()),
]

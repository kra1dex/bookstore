from django.urls import path, include
from rest_framework import routers

from products import views

router = routers.SimpleRouter()
router.register('genres', views.GenreViewSet)

urlpatterns = [
    path('', views.BookListView.as_view()),
    path('create/', views.BookCreateView.as_view()),
    path('', include(router.urls)),
]

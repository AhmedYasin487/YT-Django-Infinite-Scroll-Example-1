from django.urls import path
from .views import IndexView, BookDetailView, GenreView, AddBookView, BookEditView
from .views import redirect_view

app_name = 'books'

urlpatterns = [
    path('redirect/', redirect_view, name="books-home"),
    path('', IndexView.as_view(), name='ex2'),
    path('add/', AddBookView.as_view(), name='add'),
    path('g/<str:genre>', GenreView.as_view(), name='genre'),
    path('<slug:slug>/', BookDetailView.as_view(), name='book-detail'),
    path('<slug:slug>/edit', BookEditView.as_view(), name='edit-detail'),
]

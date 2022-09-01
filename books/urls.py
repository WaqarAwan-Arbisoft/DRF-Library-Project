from django.urls import path
from . import views
urlpatterns = [
    path("books", views.GetAddBooksView.as_view(), name="view-add-books"),
    path("books/<pk>", views.GetUpdateDeleteBookView.as_view(),
         name="get-update-destroy-book"),
    path("authors/", views.GetAddAuthorView.as_view(), name="view-add-authors"),
    path("authors/<pk>", views.getUpdateDeleteAuthorView.as_view(),
         name="get-update-destroy-author"),
]

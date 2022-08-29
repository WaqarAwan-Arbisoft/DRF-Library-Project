from django.urls import path
from . import views
urlpatterns = [
    path("books",views.ViewAddBooksView.as_view(),name="view-add-books")
]

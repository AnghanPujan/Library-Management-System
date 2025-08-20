from django.urls import path, include
from .views import new_book, edit_book, delete_book, dashboard
urlpatterns = [

    path('add/',new_book),
    path("<int:id>/edit/",edit_book),
    path("<int:id>/delete/",delete_book),
]

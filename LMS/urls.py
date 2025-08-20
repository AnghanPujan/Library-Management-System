from django.contrib import admin
from django.urls import path, include
from book.views import allbooks, home, new_author, dashboard
from members.views import all_members
from borrow.views import all_borrowed, borrow
from returnBook.views import return_book
from reports.views import overdue


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',home),
    path('books/', allbooks),
    path('books/',include('book.urls')),
    path('author/',new_author),
    path('members/',all_members),
    path('members/',include('members.urls')),
    path('borrow/',borrow),
    path('return/', return_book),
    path('dashboard/', dashboard)
]

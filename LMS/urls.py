from django.contrib import admin
from django.urls import path, include
from book.views import allbooks, new_author, dashboard
from borrow.views import borrow
from returnBook.views import return_book
from reports.views import overdue


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',dashboard),
    path('books/', allbooks),
    path('books/',include('book.urls')),
    path('author/',new_author),
    path('members/',include('members.urls')),
    path('borrow/',borrow),
    path('return/', return_book),
    path('dashboard/', dashboard),
    path('reports/',include('reports.urls'))
]

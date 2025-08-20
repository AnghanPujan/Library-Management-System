from django.shortcuts import render
from django.http import HttpResponse
from book.models import Book
from django.utils import timezone

def overdue(request):
    overdue_books = Book.objects.filter(due_date__lt=timezone.now(), is_available=False)
    context = {
        'overdue_books': overdue_books,
    }
    return render(request , "reports/allOverdue.html", context=context)
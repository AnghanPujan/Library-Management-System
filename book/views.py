from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from book.bookForms import add_book, add_author
from book.models import Book, Author, Member
from borrow.borrowForm import borrowFrom
from datetime import date
from django.utils import timezone

def home(request):
    return HttpResponse("<h1>home</h1>")

def allbooks(request):
    books = Book.objects.all()
    return render(request, "book/allBook.html", {"books": books})

def new_book(request):
    if request.method == "POST":
        form = add_book(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = add_book()
    return render(request, "book/addBook.html", {'form' : form})

def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    author_name = None
    
    if request.method == "POST":
        # No form used anymore, getting data directly from POST
        title = request.POST.get("title")
        author_name = request.POST.get("author")
        category_name = request.POST.get("category")

        # Update book attributes
        book.title = title
        book.category = category_name
        book.is_available = request.POST.get("is_available") == "on"

        # Set author
        try:
            book.author = Author.objects.get(name=author_name)
        except Author.DoesNotExist:
            return render(request, 'book/editBook.html', {
                'text': 'Author not found'
            })

        book.save()

    return render(request, 'book/editBook.html', {'book': book})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.delete()
    return render(request, "book/deleteBook.html", {"book": book})


def new_author(request):
    if request.method == "POST":
        form = add_author(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Invalid data")
    else:
        form = add_author()
    return render(request, "book/addAuthor.html", {'form' : form})

def dashboard(request):
    all_books = Book.objects.all()
    all_members = Member.objects.all()
    borrowed_books = Book.objects.filter(is_available=False) 
    overdue_books = Book.objects.filter(due_date__lt=timezone.now(), is_available=False)

    context = {
        'books': all_books,
        'members': all_members,
        'borrowed_books': borrowed_books,
        'overdue_books': overdue_books,
    }
    return render(request, "book/dashboard.html", context=context)
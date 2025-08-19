from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from book.bookForms import add_book, add_author
from book.models import Book, Author

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
    if request.method == "POST":
        form = BorrowForm(request.POST)
        if form.is_valid():
            book.title = form.cleaned_data["title"]
            author_name = form.cleaned_data["author"]
            category_name = form.cleaned_data["category"]
        else:
            return render(request,
                'book/editBook.html', 
                {
                'book': book,
                'text': 'Data Not valid'
            })
        try:
            book.author = Author.objects.get(name=author_name)
        except (Author.DoesNotExist):
            return render(request,
                'book/editBook.html', 
                {
                'book': book,
                'text': 'Author not found'
            })
        book.category = category_name
        book.is_available = request.POST.get("is_available") == "on"
        print(book.title)   
        book.save()

    return render(request, 'book/editBook.html', {'book': book,'text':"Book Updated "})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.delete()
    return render(request, "book/deleteBook.html", {"book": book})


def new_author(request):
    if request == "GET":
        form = add_author(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = add_author()
    return render(request, "book/addAuthor.html", {'form' : form})
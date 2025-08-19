from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from returnBook.returnForm import returnFrom
from book.models import Book, Member

def return_book(request):
    if request.method == "POST":
        form = returnFrom(request.POST)
        if form.is_valid():
            book_name = form.cleaned_data["book_name"]
            member_name = form.cleaned_data["member_name"]
            return_date = form.cleaned_data["return_date"]

            book = get_object_or_404(Book, title=book_name)
            member = get_object_or_404(Member, name=member_name)

            book.is_available = 1
            member.borrowed_books -= 1

            book.save()
            member.save()
        pass
    else:
        form = returnFrom()
    return render(request, "returnBook/returnBook.html", {'form': form})
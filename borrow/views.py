from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from borrow.borrowForm import borrowFrom
from book.models import Book, Member
from datetime import timedelta


def borrow(request):
    if request.method == "POST":
        form = borrowFrom(request.POST)
        if form.is_valid():
            
            book_name = form.cleaned_data["book_name"]
            member_name = form.cleaned_data["member_name"]
            issue_date = form.cleaned_data["issue_date"]
            due_date = issue_date + timedelta(days=15)
            
            try:
                book = Book.objects.get(title=book_name)
            except Book.DoesNotExist:
                return render(request, 'borrow/borrowForm.html', {
                    'form': form,
                    'msg': 'Book does not exist.'
                })

            try:
                member = Member.objects.get(name=member_name)
            except Member.DoesNotExist:
                return render(request, 'borrow/borrowForm.html', {
                    'form': form,
                    'msg': 'Member is not registred.'
                })

            if not book.is_available:
                return render(request, 'borrow/borrowForm.html', {
                    'form': form,
                    'msg': 'Book is not available.'
                })

            if member.borrowed_books >= 5:
                return render(request, 'borrow/borrowForm.html', {
                    'form': form,
                    'msg': 'Member has reached the borrow limit.'
                })

            book.issue_date = issue_date
            book.due_date = due_date
            book.member = member
            book.is_available = False
            book.save()

            member.borrowed_books += 1
            member.save()
    else:
        form = borrowFrom()

    return render(request, "borrow/borrowForm.html", {'form': form})

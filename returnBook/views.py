from django.shortcuts import render, get_object_or_404
from returnBook.returnForm import returnFrom
from book.models import Book, Member
from datetime import datetime

def return_book(request):
    if request.method == "POST":
        form = returnFrom(request.POST)
        if form.is_valid():
            book_name = form.cleaned_data["book_name"]
            member_name = form.cleaned_data["member_name"]
            return_date = form.cleaned_data["return_date"] 
            try:
                book = Book.objects.get(title=book_name)
            except Book.DoesNotExist:
                return render(request, 'borrow/borrowForm.html', {
                    'form': form,
                    'msg': 'Book does not from our store.'
                })
            try:
                member = Member.objects.get(name=member_name)
            except Member.DoesNotExist:
                return render(request, 'borrow/borrowForm.html', {
                    'form': form,
                    'msg': 'Member is not registed.'
                })
            book.is_available = True
            member.borrowed_books -= 1  
            book.return_date = return_date
           
            FINE_PER_DAY = 15 
            due_date = book.due_date 

            if return_date > due_date:
                late_days = (return_date - due_date).days
                fine = late_days * FINE_PER_DAY
                msg = f"Book returned late by {late_days} days. Fine: ₹{fine}"
                book.save()
                member.save()
                return render(request, "returnBook/returnBook.html", {'form': form,'text': msg} )
            else:
                msg = "Book returned on time."
                book.save()
                member.save()
                return render(request, "returnBook/returnBook.html", {'form': form, 'text':msg})
        
    else:
        form = returnFrom()
    
    return render(request, "returnBook/returnBook.html", {'form': form})

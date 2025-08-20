from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
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
            
            book = get_object_or_404(Book, title=book_name)
            member = get_object_or_404(Member, name=member_name)

          
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

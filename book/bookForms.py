from django import forms
from .models import Book, Author, Member

class add_book(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'category', 'author']

class edit_book(forms.Form):
    pass

class add_author(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class add_member(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name','email','join_date']
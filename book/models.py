from django.db import models
from datetime import date

class Author(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=80, unique=True)
    join_date = models.DateField(default=date.today)
    borrowed_books = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    member = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, blank=True)
    issue_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
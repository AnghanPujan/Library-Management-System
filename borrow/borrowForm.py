from django import forms

class borrowFrom(forms.Form):
    book_name = forms.CharField()
    member_name = forms.CharField()
    issue_date = forms.DateField()
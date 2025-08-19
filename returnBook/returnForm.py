from django import forms

class returnFrom(forms.Form):
    book_name = forms.CharField()
    member_name = forms.CharField()
    return_date = forms.DateField()

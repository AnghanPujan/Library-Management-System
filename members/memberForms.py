from django import forms
from book.models import Member

class add_member(forms.ModelForm):
    class Meta:
        model =  Member
        fields = ['name', 'email', 'join_date']

from django.shortcuts import render
from django.http import HttpResponse
from members.memberForms import add_member
from book.models import Member

def all_members(request):
    all_members = Member.objects.all()
    context = {
        'members': all_members,
    }
    return render(request, "members/allMembers.html", context=context)

def new_member(request):
    if request.method == "POST":
        form = add_member(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = add_member()
    return render(request, "members/addMember.html", {'form' : form})
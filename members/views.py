from django.shortcuts import render
from django.http import HttpResponse
from members.memberForms import add_member

def all_members(request):
    return HttpResponse("<h1>In all member page<h1>")

def new_member(request):
    if request.method == "POST":
        form = add_member(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = add_member()
    return render(request, "members/addMember.html", {'form' : form})
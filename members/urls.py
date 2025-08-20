from django.urls import path
from members.views import all_members, new_member

urlpatterns = [ 
    path('all/',all_members),
    path('add/', new_member),
]
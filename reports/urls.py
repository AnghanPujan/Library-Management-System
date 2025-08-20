from django.urls import path
from reports.views import overdue

urlpatterns = [
    path('overdue/',overdue)
]

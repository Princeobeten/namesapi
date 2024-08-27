from django.urls import path
from .views import NameListView

urlpatterns = [
    path('names/', NameListView.as_view(), name='name-list'),
]
from rest_framework import generics
from .models import Name
from .serializers import NameSerializer

class NameListView(generics.ListCreateAPIView):
    queryset = Name.objects.all()
    serializer_class = NameSerializer
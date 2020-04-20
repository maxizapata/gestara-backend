from rest_framework import generics
from .models import Cooperative, Category
from .serializer import CooperativeSerializer, CategoriesSerializer


class CooperativeApiView(generics.ListAPIView):
    queryset = Cooperative.objects.all().order_by('name')
    serializer_class = CooperativeSerializer


class CategoriesApiView(generics.ListAPIView):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategoriesSerializer

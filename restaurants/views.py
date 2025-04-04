from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Restaurant
from .serializers import RestaurantSerializer


# Create your views here.
class RestaurantCreateAPIView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]

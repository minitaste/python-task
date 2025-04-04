from django.urls import path

from . import views

urlpatterns = [
    path("restaurants/", views.RestaurantCreateAPIView.as_view(), name="restaurants"),
]

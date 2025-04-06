from datetime import date

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Menu, Vote
from .serializers import MenuSerializer, MenuV2Serializer, VoteSerializer


class MenuCreateAPIView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class TodayMenuView(APIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.version == "v2":
            return MenuV2Serializer
        return MenuSerializer

    def get(self, request, format=None):
        today = date.today()
        menus = Menu.objects.filter(date=today)

        if not menus.exists():
            return Response(
                {"detail": "No menu found for today."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer_class = self.get_serializer_class()
        serializer = serializer_class(menus, many=True)

        return Response({"date": today, "results": serializer.data})


class TodayResultView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        today = date.today()
        menus = Menu.objects.filter(date=today)

        if not menus.exists():
            return Response(
                {"detail": "No menu found for today."}, status=status.HTTP_404_NOT_FOUND
            )

        results = []

        for menu in menus:
            vote_count = Vote.objects.filter(menu=menu).count()

            results.append(
                {
                    "id": menu.pk,
                    "restaurant": menu.restaurant.name,
                    "menu": menu.menu_data,
                    "vote_count": vote_count,
                }
            )

        return Response({"date": today, "results": results})


class VoteCreateAPIView(generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = []

from django.urls import path

from . import views

urlpatterns = [
    path("menus/", views.MenuCreateAPIView.as_view(), name="menus"),
    path("menus/today/", views.TodayMenuView.as_view(), name="today-menu"),
    path(
        "menus/today/results/",
        views.TodayResultView.as_view(),
        name="today-menu-results",
    ),
    path("votes/", views.VoteCreateAPIView.as_view(), name="add-vote")
]

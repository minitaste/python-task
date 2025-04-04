from django.urls import path

from . import views

urlpatterns = [
    path("employees/", views.EmployeeCreateAPIView.as_view(), name="create-employee")
]

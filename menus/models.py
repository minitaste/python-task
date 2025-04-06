from django.db import models

from employees.models import Employee
from restaurants.models import Restaurant


class Menu(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="menus"
    )
    date = models.DateField()
    menu_data = models.JSONField()

    class Meta:
        unique_together = ("restaurant", "date")

    def __str__(self):
        return f"{self.restaurant.name} - {self.date}"


class Vote(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="votes"
    )
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="votes")

    class Meta:
        unique_together = ("employee", "menu")

    def __str__(self):
        return f"{self.employee.username} - {self.menu}"

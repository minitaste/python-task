from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            "username",
            "password",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=Employee.objects.all(),
                        message="Username already taken.",
                    )
                ]
            },
        }

    def create(self, validated_data):
        return Employee.objects.create_user(**validated_data)

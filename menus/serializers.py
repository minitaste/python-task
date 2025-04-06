from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Menu, Vote


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ("menu",)
        read_only_fields = ("id",)

    def validate(self, data):
        employee = self.context["request"].user
        menu = data.get("menu")

        if Vote.objects.filter(employee=employee, menu=menu).exists():
            raise ValidationError(
                {"details": "You have already voted for this menu today."}
            )

        return data

    def create(self, validated_data):
        validated_data["employee"] = self.context["request"].user
        return super().create(validated_data)


class MenuV2Serializer(serializers.ModelSerializer):
    vote_count = serializers.IntegerField(source="votes.count", read_only=True)
    voters = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ["id", "restaurant", "date", "menu_data", "vote_count", "voters"]

    def get_voters(self, obj):
        return [vote.employee.username for vote in obj.votes.all()]

from rest_framework import serializers
from gamerauntsia.gamer.models import GamerUser


class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamerUser
        fields = ("id", "username", "getFullName", "email")


class UsersUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamerUser
        fields = ("getFullName", "email")


class UsersCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamerUser
        fields = ("getFullName", "email")

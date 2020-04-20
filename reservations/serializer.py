from rest_framework import serializers
from .models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    cooperative = serializers.CharField
    date = serializers.DateTimeField

    def create(self, validated_data):
        return Reservation.objects.create(**validated_data)

from rest_framework import serializers
from django.utils import timezone
from images.serializers import ImageSerializer
from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    ticket_images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = "__all__"

    def create(self, validated_data):
        validated_data["creation_date"] = timezone.now()
        validated_data["created_by"] = self.context.get("request").user
        return super().create(validated_data)

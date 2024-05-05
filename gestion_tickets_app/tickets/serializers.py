from .models import Ticket
from rest_framework import serializers
from django.utils import timezone

class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = '__all__'
    
    
    def create(self, validated_data):
        validated_data['creation_date'] = timezone.now()
        validated_data['created_by'] = self.context.get('request').user
        return super().create(validated_data)

"""Serializer for the Token auth."""
from rest_framework import serializers
from django.contrib.auth import authenticate

class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=username,
            password=password
        )
        if not user:
            raise serializers.ValidationError('No fue posible autenticarse')

        attrs['user'] = user
        return attrs

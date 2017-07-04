from django.contrib.auth.models import User, Group
from rest_framework import serializers
from client.models import ClientConfig

class ClientConfigSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    identifier = serializers.CharField(max_length=150, required=True)

    def create(self, validated_data):
        return ClientConfig.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.description = validated_data.get('identifier', instance.description)

        instance.save()
        return instance
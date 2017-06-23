from django.contrib.auth.models import User, Group
from rest_framework import serializers
from server.models import Client

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
   
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ClientSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(max_length=150, required=True)
    address = serializers.CharField(max_length=500, required=True)
    host_address = serializers.CharField(max_length=150, required=True)

    def create(self, validated_data):
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.address = validated_data.get('address', instance.address)
        instance.host_address = validated_data.get('host_address', instance.host_address)

        instance.save()
        return instance
        

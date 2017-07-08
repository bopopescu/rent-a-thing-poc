from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import Rental


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
   
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class RentalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    tenant_user = 

    def create(self, validated_data):
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.address = validated_data.get('address', instance.address)
        instance.host_address = validated_data.get('host_address', instance.host_address)

        instance.save()
        return instance

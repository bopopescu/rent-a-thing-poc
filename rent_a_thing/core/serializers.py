from django.contrib.auth.models import User, Group
from rest_framework import serializers
from core.models import Rental, RentalObject
from server.serializers import ClientSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
   
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class RentalObjectSerializer(serializers.Serializer):
    id = serializers.UUIDField(format='hex_verbose')
    current_tenant_user = serializers.UserSerializer(many=False)

class RentalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    tenant_user = UserSerializer(many=False)
    rented_object = RentalObjectSerializer(many=False)
    is_confirmed = serializers.BooleanField()
    rental_station = ClientSerializer(many=False)
    return_station = ClientSerializer(many=False)
    rental_date = serializers.DateTimeField()
    return_date = serializers.DateTimeField()


    def create(self, validated_data):
        return Rental.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.tenant_user = validated_data.get('tenant_user', instance.tenant_user)
        instance.rented_object = validated_data.get('rented_object', instance.rented_object)
        instance.is_confirmed = validated_data.get('is_confirmed', instance.is_confirmed)
        instance.rental_station = validated_data.get('rental_station', instance.rental_station)
        instance.rental_date = validated_data.get('rental_date', instance.rental_date)
        instance.return_station = validated_data.get('return_station', instance.return_station)
        instance.return_date = validated_data.get('return_date', instance.return_date)

        instance.save()
        return instance

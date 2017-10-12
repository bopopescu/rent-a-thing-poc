import datetime

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from core.models import Rental, RentalObject, Client, Profile, Price, Wallet


class PriceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Price
        fields = ('value',)

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('cpf','address1','address2','zipcode')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    profile = ProfileSerializer(many=False)

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password', 'profile', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
   
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class RentalObjectSerializer(serializers.Serializer):
    id = serializers.UUIDField(format='hex_verbose')
    station_id = serializers.IntegerField()
    is_return = serializers.BooleanField()
    rental_cost = serializers.IntegerField()
    current_tenant = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    def update(self, instance, validated_data):

        client = Client.objects.get(id=validated_data['station_id'])
        rental_object = RentalObject.objects.get(id=validated_data['id'])
        is_return = validated_data['is_return']


        if is_return == False:
            instance.current_station = None
            instance.current_tenant = validated_data['current_tenant']

            Rental.objects.create(tenant_user=validated_data['current_tenant'],
                                  rental_date = datetime.datetime.now(),
                                  rental_station= client,
                                  rented_object=rental_object)
        else:
            instance.current_tenant = None
            instance.current_station = client

            wallet = Wallet.objects.get(id=validated_data['current_tenant'])
            wallet.balance -= validated_data['rental_cost']
            wallet.save()

            Rental.objects.filter(tenant_user=validated_data['current_tenant']).delete()

        instance.save()

        #TODO: Plugar chamada ao stepper.

        return instance

class ClientSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(max_length=150, required=True)
    address = serializers.CharField(max_length=500, required=True)
    host_address = serializers.CharField(max_length=150, required=True)
    rental_objects = RentalObjectSerializer(many=True)

    def create(self, validated_data):
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.address = validated_data.get('address', instance.address)
        instance.host_address = validated_data.get('host_address', instance.host_address)

        instance.save()
        return instance

class RentalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    tenant_user = UserSerializer(many=False)
    rented_object = RentalObjectSerializer(many=False)
    #is_confirmed = serializers.BooleanField()
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

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status, mixins
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

from core.models import Client, Transaction, Wallet, RentalObject, Rental
from core.serializers import ClientSerializer, RentalObjectSerializer, RentalSerializer
from server.serializers import TransactionSerializer, WalletSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = None

    @csrf_exempt
    def list_all(self, request):
        if request.method == 'GET':
            clients = Client.objects.all()
            serializer = ClientSerializer(clients, many=True)
            return JsonResponse(serializer.data, safe=False)

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    pagination_class = None

class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    pagination_class = None

class RentalObjectViewSet(UpdateAPIView, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = RentalObject.objects.all()
    serializer_class = RentalObjectSerializer
    pagination_class = None

class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    pagination_class = None

    def retrieve(self, request, *args, **kwargs):
        queryset = Rental.objects.all()
        filter = queryset.filter(tenant_user = kwargs['pk'])

        if filter.count() > 0:
            rental = filter[0]
            serializer = RentalSerializer(rental, context={'request': request})
            return Response(serializer.data)

        return Response(None, status=status.HTTP_404_NOT_FOUND)

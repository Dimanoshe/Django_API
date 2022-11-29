from rest_framework import viewsets, permissions
from .serializers import *
from django.contrib.auth.models import User
from rest_framework import generics
import pandas as pd
from django.shortcuts import redirect
from .bills_validator import bills_validator, clients_validator
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class BillsViewSet(viewsets.ModelViewSet):
    queryset = Bills.objects.all()
    serializer_class = BillsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client', 'client_org']

class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer


class BillsUploadAPIView(generics.CreateAPIView):
    queryset = Bills.objects.all()
    serializer_class = BillsUploadSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        new_tabl = pd.read_csv(file)

        # Add Clients
        clients_set = set(new_tabl['client_name'])
        for client in clients_set:
            if clients_validator(client) == False:
                continue
            new_row = Clients(client_name = client)
            try:            
                new_row.save()
            except Exception as ex:
                if ex == 'This client_name already exists':
                    continue

        # Add Bills
        for _, row in new_tabl.iterrows():
            if bills_validator(row) == False:
                continue
            client_object = Clients.objects.get(client_name=row["client_name"])
            new_row = Bills(
                    client = client_object,
                    client_org = row["client_org"],
                    number = row['№'],
                    date = row["date"],
                    service = row["service"],
                    bills_sum = float(row['sum'].replace(',', '.'))
                    )
            try:            
                new_row.save()
            except Exception as ex:
                if ex == 'This client-number pair already exists':
                    continue
        return redirect("bills-list")
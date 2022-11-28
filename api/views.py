from rest_framework import viewsets, permissions
from .serializers import *
from django.contrib.auth.models import User
from rest_framework import generics
import pandas as pd
from django.shortcuts import redirect
from .bills_validator import validator


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class BillsViewSet(viewsets.ModelViewSet):
    queryset = Bills.objects.all()
    serializer_class = BillsSerializer
    permission_classes = [permissions.IsAuthenticated]


class BillsUploadAPIView(generics.CreateAPIView):
    queryset = Bills.objects.all()
    serializer_class = BillsUploadSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        new_tabl = pd.read_csv(file)

        for _, row in new_tabl.iterrows():
            if validator(row) == False:
                continue
            new_file = Bills(
                       client_name = row['client_name'],
                       client_org= row["client_org"],
                       number= row['№'],
                       date= row["date"],
                       service= row["service"],
                       bills_sum = float(row['sum'].replace(',', '.'))
                       )
            try:            
                new_file.save()
            except Exception as ex:
                if ex == 'This client-number pair already exists':
                    continue
        return redirect("bills-list")
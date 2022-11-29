from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class BillsUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillsUpload
        fields = '__all__'

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'

class BillsSerializer(serializers.ModelSerializer):
    client = ClientsSerializer()
    class Meta:
        model = Bills
        fields = '__all__'
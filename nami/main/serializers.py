from dataclasses import field
from rest_framework import serializers
from main.models import Namiwallet

class NamiwalletSerializer(serializers.ModelSerializer):
    class Meta:
        model=Namiwallet
        fields='__all__'
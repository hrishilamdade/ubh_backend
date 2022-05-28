from rest_framework import serializers
from .models import *

class EmpanelmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empanelment
        fields = '__all__'
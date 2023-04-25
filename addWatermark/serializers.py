
from rest_framework import serializers
from .models import BaseData

class BaseDataSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=False)

    class Meta:
        model = BaseData
        fields = '__all__'
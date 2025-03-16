from rest_framework import serializers, viewsets
from .models import WhatsUsers

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)  # Returns full URL

    class Meta:
        model = WhatsUsers
        fields ='__all__'

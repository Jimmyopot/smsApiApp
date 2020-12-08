from rest_framework import serializers

from .models import CemanetEndpoint


class CemanetEndpointSerializers(serializers.ModelSerializer):
    class Meta:
        model = CemanetEndpoint
        fields = ["api_key", "api_secret", "unique_ref", "clientId", "productId", "phone_no", "message" ]
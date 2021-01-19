from rest_framework import serializers
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample


class TreeInputSerialier(serializers.Serializer):
    data = serializers.ListField(child=serializers)

from dataclasses import field
import imp
from rest_framework.serializers import ModelSerializer
from base.models import Room


class RoomSerializer(ModelSerializer):
    class Meta:
        model= Room
        fields='__all__'
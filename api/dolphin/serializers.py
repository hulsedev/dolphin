from rest_framework import serializers

from dolphin.models import Log


class LogSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)

    def create(self, validated_data):
        return Log.objects.create(**validated_data)

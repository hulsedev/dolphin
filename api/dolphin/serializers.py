from rest_framework import serializers

from dolphin.models import Log, Machine


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = "__all__"

    def create(self, validated_data):
        return Machine.objects.create(**validated_data)


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = "__all__"

    def create(self, validated_data):
        return Log.objects.create(**validated_data)
